import numpy as np
import regex as re


def move_1(positions, iterations, from_i, to_i):
    for i in range(iterations):
        # Add box to new stack
        positions[to_i-1].append(positions[from_i-1][-1])
        # Remove box from old stack
        positions[from_i-1].pop(-1)
    return positions


def move_2(positions, iterations, from_i, to_i):
    # Add boxes to new stack
    positions[to_i-1] += positions[from_i-1][-iterations:]
    # Remove boxes from old stack
    positions[from_i-1] = positions[from_i-1][:-(iterations)]
    
    return positions


def move_boxes(filepath, move=1):

    # Read input data
    with open(filepath) as f:
        positions = []
        for line in f:
            # Until the row of numbers, read the starting position
            if line.strip().startswith('1'):
                # Rotate and remove empty slots
                positions = np.rot90(np.array(positions), k=3).tolist()
                positions = [list(filter(lambda x: x!= ' ', row)) for row in positions]
                # Read the rest of the file
                rest = f.read()
                break
            # Append all values in the boxes, and spaces where there aren't any boxes
            positions.append([line[letter_i] for letter_i in range(1, len(line), 4)])
    # Extract the instructions (move, from, to)
    instructions = re.findall('move (\d+) from (\d+) to (\d+)\n*', rest)

    # Perform instructions
    for instruction in instructions:
        if move == 1:
            positions = move_1(positions, int(instruction[0]), int(instruction[1]), int(instruction[2]))
        elif move == 2:
            positions = move_2(positions, int(instruction[0]), int(instruction[1]), int(instruction[2]))
        else:
            raise ValueError('Invalid moving strategy, should be 1 or 2')
    
    return ''.join([row[-1] for row in positions])


if __name__ == "__main__":
    filepath="data/day5.txt"
    # filepath="data/test_day5.txt"

    print(f"The top crates in first strategy are: {move_boxes(filepath, move=1)}")
    print(f"The top crates in second strategy are: {move_boxes(filepath, move=2)}")