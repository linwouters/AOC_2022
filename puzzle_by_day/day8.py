# AOC 2022-12-08
# Lin Wouters

def do_stuff(filepath):
    with open(filepath) as f:
        for line in f:
            print(line.strip())

    return True

if __name__ == "__main__":
    filepath="../data/day8.txt"
    filepath="../data/test_day8.txt"

    total_size, remove_size = do_stuff(filepath)
    print(f"The total size of the folders with max 100000 size is: {total_size}")
    print(f"The size of the smallest folder that can be removed to clear enough space is: {remove_size}")