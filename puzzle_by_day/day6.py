
def subroutine(filepath, num_distinct=4):

    # Read input data
    with open(filepath) as f:
        line = f.read().strip()
        for i in range(num_distinct, len(line), 1):
           if len(set(line[i-num_distinct:i])) == num_distinct:
                return i

    return False


if __name__ == "__main__":
    filepath="data/day6.txt"
    # filepath="data/test_day5.txt"

    print(f"The top crates in first strategy are: {subroutine(filepath, num_distinct=4)}")
    print(f"The top crates in first strategy are: {subroutine(filepath, num_distinct=14)}")