import re


def main():
    total_sum = 0
    mul_enabled = True
    mul_pattern = re.compile(r'mul\((\d+),\s*(\d+)\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")

    file_path = r'C:\Users\Rafae\Code\AdventOfCode_2024\Day_3\input.txt'
    with open(file_path, 'r') as file:
        content = file.read()

    parts = re.split(r'(do\(\)|don\'t\(\))', content)
    for part in parts:
        if do_pattern.fullmatch(part):
            mul_enabled = True
        elif dont_pattern.fullmatch(part):
            mul_enabled = False
        elif mul_enabled:
            matches = mul_pattern.findall(part)
            for match in matches:
                if len(match) == 2:
                    total_sum += int(match[0]) * int(match[1])

    print(total_sum)


if __name__ == "__main__":
    main()
