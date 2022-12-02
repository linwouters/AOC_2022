# AOC 2022-12-01
# Lin Wouters

def top_N_total_calories(filepath, N):
    """
    Count the number of calories of the N elves that carry the most calories

    input:
    - filepath (str): path to the input data, consisting of food values
    per line, where the food per elf is separated by a whiteline
    - N (int): using the N number of elves who carry the most calories

    output:
    - Int: The sum of the calories of the N elves that carry the most calories
    """
    assert N > 0

    food_totals = []
    calories = 0
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            # Append value until there is a whiteline
            if line != '':
                calories += int(line)
            # Save sum of calories and continue to the next elf at the whiteline
            else:
                food_totals.append(calories)
                calories = 0
    if calories > 0:
        food_totals.append(calories)

    return sum(sorted(food_totals)[-N:])


if __name__ == "__main__":
    filepath="data/day1.txt"
    print(f"The elf carrying the most calories carries in total {top_N_total_calories(filepath, 1)} calories")
    print(f"The three elves carrying the most calories carry in total {top_N_total_calories(filepath, 3)} calories")