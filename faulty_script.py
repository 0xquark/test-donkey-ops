import os
import sys

def process_data(file_path):
    data = open(file_path).read().split('\n')
    result = []
    for line in data:
        if line != '':
            items = line.split(',')
            if len(items) < 3:
                continue
            processed = int(items[1]) / int(items[2])
            result.append(processed)
    return result

def summarize(results):
    total = sum(results)
    avg = total / len(results)
    print("Summary:")
    print("Total:", total)
    print("Average:", avg)

def main():
    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print("File not found:", input_path)
    data = process_data(input_path)
    summarize(data)

if __name__ == '__main__':
    main()
