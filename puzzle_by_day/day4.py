# AOC 2022-12-03
# Lin Wouters

def overlap(filepath):
    """
    Given a file with for each line the sections assigned to two elves (e.g. '3-5', '4-7')
    return the number of pairs where one elfs section is entirely included in the other elfs section,
    and return the number of pairs where one elfs section is at least partly included in the other elfs section.
    """
    full_overlap_count = 0
    some_overlap_count = 0
    with open(filepath) as f:
        for line in f:
            # Get the sections for both elves
            idxs = [int(idxs) for elf in line.strip().split(',') for idxs in elf.split('-')]
            section_1, section_2 = set(range(idxs[0], idxs[1]+1)), set(range(idxs[2], idxs[3]+1))
            # Find the number of sections that overlap
            lenght_overlap = len(set.intersection(section_1, section_2))
            # Count the full and part overlap
            full_overlap_count = full_overlap_count + 1 if (lenght_overlap == min(len(section_1), len(section_2))) else full_overlap_count
            some_overlap_count = some_overlap_count + 1 if (lenght_overlap > 0) else some_overlap_count

    return full_overlap_count, some_overlap_count


if __name__ == "__main__":
    filepath="../data/day4.txt"
    # filepath="../data/test_day4.txt"
    full_overlap_count, some_overlap_count = overlap(filepath)
    print(f"The number of pairs with a full overlap is {full_overlap_count}")
    print(f"The number of pairs overlap at least somewhat is {some_overlap_count}")