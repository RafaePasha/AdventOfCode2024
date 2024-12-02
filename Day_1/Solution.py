import os
import math


def main():
    file_path = r"C:\Users\Rafae\Code\AdventOfCode_2024\Day_1\input.txt"

    with open(file_path, "r") as file:
        lines = file.readlines()

    list1, list2 = zip(*(map(int, line.strip().split("   "))
                       for line in lines if line.strip()))

    list1 = sorted(list1)
    list2 = sorted(list2)

    total_distance = sum(math.dist([val1], [val2])
                         for val1, val2 in zip(list1, list2))

    print(total_distance)


if __name__ == "__main__":
    main()
