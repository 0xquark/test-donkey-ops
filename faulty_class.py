import json
import datetime

class User:
    def __init__(self, username, created_at):
        self.username = username
        self.created_at = created_at
        self.is_active = True

    def deactivate(self):
        self.is_active = False

class Admin(User):
    def __init__(self, username, created_at, permissions=[]):
        super().__init__(username, created_at)
        self.permissions = permissions

    def add_permission(self, perm):
        if perm not in self.permissions:
            self.permissions.append(perm)

def load_users(file_path):
    f = open(file_path, 'r')
    data = json.load(f)
    users = []
    for u in data['users']:
        if u['type'] == 'admin':
            user = Admin(u['username'], u['created_at'], u['permissions'])
        else:
            user = User(u['username'], u['created_at'])
        users.append(user)
    return users

def generate_report(users):
    report = {}
    for u in users:
        age = datetime.datetime.now() - datetime.datetime.strptime(u.created_at, "%Y-%m-%d")
        report[u.username] = {
            "active": u.is_active,
            "account_age_days": age.days
        }
        if isinstance(u, Admin):
            report[u.username]["permissions"] = u.permissions
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    path = "users.json"
    users = load_users(path)
    generate_report(users)
