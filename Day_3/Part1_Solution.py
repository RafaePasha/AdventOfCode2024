import re


def main():
    pattern = re.compile(r'mul\((\d+),\s*(\d+)\)')
    file_path = r'C:\Users\Rafae\Code\AdventOfCode_2024\Day_3\input.txt'

    with open(file_path, 'r') as file:
        content = file.read()

    total_sum = sum(int(match[0]) * int(match[1])
                    for match in pattern.findall(content))

    print(total_sum)


if __name__ == "__main__":
    main()
