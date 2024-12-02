def isValid(values):
    return all(0 < values[i] - values[i-1] <= 3 for i in range(1, len(values))) or \
        all(0 < values[i-1] - values[i] <= 3 for i in range(1, len(values)))


def main():
    file_path = r'C:\Users\Rafae\Code\AdventOfCode_2024\Day_2\Input.txt'

    with open(file_path, "r") as file:
        reports = [report.rstrip() for report in file]

    valid_reports = [
        report for report in reports
        if isValid(list(map(int, report.split(" "))))
    ]

    print(f"Number of valid reports: {len(valid_reports)}")


if __name__ == "__main__":
    main()
