import re


def main():
    total_sum = 0
    pattern = re.compile(r'mul\((\d+),\s*(\d+)\)')

    with open(r'C:\Users\Rafae\Code\AdventOfCode_2024\Day_3\input.txt', 'r') as file:
        for line in file:
            matches = pattern.findall(line)
            for match in matches:
                total_sum += int(match[0]) * int(match[1])

    print(total_sum)


if __name__ == "__main__":
    main()
