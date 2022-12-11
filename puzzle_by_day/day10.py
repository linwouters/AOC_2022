# AOC 2022-12-07
# Lin Wouters

import numpy as np

def sum_signal_strength(filepath, start=20, steps=40):
    # Save signal at the end of the i'th cycle
    cycles = [1]
    with open(filepath) as f:
        file = f.read().strip().replace('noop', '1 0').replace('addx', '2').split('\n')
        # Iterate over commands
        for i, line in enumerate(file):
            num_cyc, signal = line.split(' ')
            # For the cycles until the command has finished
            for j in range(int(num_cyc)-1):
                cycles.append(cycles[-1])
            # For the cycle when the command has finished
            cycles.append(cycles[-1]+int(signal))

    return sum([cycles[i-1]*i for i in range(len(cycles)) if ((i + 20) % 40) == 0])


def draw(filepath):
    CRT_row = []
    sprite_pos = [0, 1, 2]
    X_value = 1
    with open(filepath) as f:
        file = f.read().strip().replace('noop', '1 0').replace('addx', '2').split('\n')
        # Iterate over commands
        for i, line in enumerate(file):
            num_cyc, signal = line.split(' ')
            
            # During execution
            for j in range(int(num_cyc)-1):
                # Draw during this cycle
                CRT_row.append(1) if (len(CRT_row)) % 40 in sprite_pos else CRT_row.append(0)

            # Draw during this cycle
            CRT_row.append(1) if (len(CRT_row)) % 40 in sprite_pos else CRT_row.append(0)
            # End execution
            X_value += int(signal)
            sprite_pos = [X_value-1, X_value, X_value+1]

    grid = np.reshape(np.array(CRT_row, dtype=object), (-1, 40))
    print(str(grid).replace('0', '.').replace('1', '#').replace('\n', '').replace(']', ']\n'))



if __name__ == "__main__":
    filepath="../data/day10.txt"
    # filepath="../data/test_day10.txt"
    # filepath="../data/test_day10_2.txt"

    total_stength = sum_signal_strength(filepath)
    print(f"The total size of the folders with max 100000 size is: {total_stength}")
    draw(filepath)
