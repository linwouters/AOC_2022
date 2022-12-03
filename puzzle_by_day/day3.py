# AOC 2022-12-03
# Lin Wouters

def get_priorities_wrongly_packed(filepath):
    """
    Return the sum of the priorities of the wrongly packed items, given the filepath to the rucksacks.
    Each line contains the packing info of a single rucksack, where the 
    first half is in the first compartment, second half in the second compartment.
    The lower case items (a-z) have priority 1-26, the capitals (A-Z) have priority 27-52.
    """
    priorities = 0
    with open(filepath) as f:
        for line in f:
            # Get the item type wrongly packed in both compartments
            wrong_item = list(set(line[:len(line)//2]).intersection(set(line[len(line)//2:])))[0]
            # Add the priority of this item type to the sum
            priorities += ord(wrong_item) - 96 if wrong_item.islower() else ord(wrong_item) - 38
    
    return priorities


def get_batch_priorities(filepath):
    """
    Return the sum of the priorities of the batch items, given the filepath to the rucksacks.
    The elves are sorted in groups of three, presented as three consecutive lines.
    Each line contains the packing info of a single rucksack, 
    and the batch item is the item that is present in every groupmember.
    The lower case items (a-z) have priority 1-26, the capitals (A-Z) have priority 27-52.
    """
    priorities = 0
    with open(filepath) as f:
        file = f.read().split('\n')
        # Iterate over the lines in groups of 3
        for start_idx in range(0, len(file)-1, 3):
            # Get the intersection of each of the three lines in that group
            batch_item = list(set(file[start_idx]).intersection(set(file[start_idx+1])).intersection(set(file[start_idx+2])))[0]
            # Add the priority of this item type to the sum
            priorities += ord(batch_item) - 96 if batch_item.islower() else ord(batch_item) - 38

    return priorities


if __name__ == "__main__":
    filepath="../data/day3.txt"
    # filepath="../data/test_day3.txt"
    print(f"The sum of the priorities of the wrongly packed items is {get_priorities_wrongly_packed(filepath)}")
    print(f"The sum of the priorities of the batches is {get_batch_priorities(filepath)}")
