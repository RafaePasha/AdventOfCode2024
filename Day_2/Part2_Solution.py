

def isValid(values):
    return all(0 < values[i] - values[i-1] <= 3 for i in range(1, len(values))) or \
        all(0 < values[i-1] - values[i] <= 3 for i in range(1, len(values)))


def canBeMadeValid(values):
    for i in range(len(values)):
        new_values = values[:i] + values[i+1:]
        if isValid(new_values):
            return True
    return False


def main():
    with open(r'C:\Users\Rafae\Code\AdventOfCode_2024\Day_2\Input.txt', "r") as file:
        reports = [report.rstrip() for report in file]

        valid_reports = []
        for report in reports:
            report_vals = report.split(" ")
            values = list(map(int, report_vals))
            if isValid(values) or canBeMadeValid(values):
                valid_reports.append(report)

    print(f"Number of valid reports: {len(valid_reports)}")


if __name__ == "__main__":
    main()
