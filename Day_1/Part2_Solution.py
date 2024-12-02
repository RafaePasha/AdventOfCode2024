from collections import Counter


def main():
    file_path = r"C:\Users\Rafae\Code\AdventOfCode_2024\Day_1\input.txt"

    with open(file_path, "r") as file:
        lines = file.readlines()

    list1, list2 = zip(*(map(int, line.strip().split("   "))
                       for line in lines if line.strip()))

    list2_counter = Counter(list2)

    similarity_score = sum(val * list2_counter[val] for val in list1)

    print(similarity_score)


if __name__ == "__main__":
    main()
