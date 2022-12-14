# Lin Wouters
# 14-12-2022

import numpy as np

def add_rocks(start, end):
    """Return the list of positions of rocks between the start and end position"""

    # If rocks in x direction
    if start[0] != end[0] and start[1] == end[1]:
        x_pos = range(min(start[0], end[0]), max(start[0], end[0])+1)
        return zip(x_pos, [start[1]]*len(x_pos))
    # If rocks in y directions
    elif start[0] == end[0] and start[1] != end[1]:
        y_pos = range(min(start[1], end[1]), max(start[1], end[1])+1)
        return zip([start[0]]*len(y_pos), y_pos)
    else:
        raise ValueError('Diagonal direction of rocks??')


def simulate_sand_part1(rock_positions, start_pos, lower_boundary):
    # Simulate falling sand
    sand_count = 0
    sand_pos = start_pos
    sand_moving = True
    counter = 0
    while True:
        # Try to move sand until it rest
        while sand_moving:
            sand_moving = False
            for direction in [np.array([0, 1]), np.array([-1, 1]), np.array([1, 1])]:
                # Sand can move in direction
                if not tuple(sand_pos + direction) in rock_positions:
                    sand_pos = sand_pos + direction
                    sand_moving = True
                    break
            # If sand falls into the abyss
            if sand_pos[1] >= lower_boundary:
                return sand_count

        # If sand rests, save the sands position and let another unit fall
        sand_count += 1
        rock_positions.add(tuple(sand_pos))
        sand_pos = start_pos
        sand_moving = True


def simulate_sand_part2(rock_positions, start_pos, lower_boundary, floor_limit):
    # Simulate falling sand
    sand_count = 0
    sand_pos = start_pos
    sand_moving = True

    while True:
        # Try to move sand until it rest
        while sand_moving:
            sand_moving = False
            for direction in [np.array([0, 1]), np.array([-1, 1]), np.array([1, 1])]:
                # Sand can move in direction
                if not tuple(sand_pos + direction) in rock_positions:
                    sand_pos = sand_pos + direction

                    # Dynamically increase floor if it nears the edge
                    if sand_pos[0] <= floor_limit[0]+1:
                        rock_positions.add((floor_limit[0]-1, lower_boundary+2))
                        floor_limit[0] -= 1
                    if sand_pos[0] >= floor_limit[1]-1:
                        rock_positions.add((floor_limit[1]+1, lower_boundary+2))
                        floor_limit[1] += 1

                    # Continue moving
                    sand_moving = True
                    break

            # If sand falls into the abyss
            if sand_pos[1] >= (lower_boundary+2):
                return ValueError(f'Sand fall below the floor at position {sand_pos}')

        # If sand rests, save the sands position and let another unit fall
        sand_count += 1
        rock_positions.add(tuple(sand_pos))
        if (sand_pos == start_pos).all():
            return sand_count
        sand_pos = start_pos
        sand_moving = True


def simulate_sand(filepath, start_pos=np.array([500, 0]), part=1):
    rock_positions = []

    # Save positions of the rock
    with open(filepath) as f:
        for line in f:
            rock_lines = line.strip().split(' -> ')
            for rock_i in range(1, len(rock_lines)):
                rock_positions += add_rocks(eval(rock_lines[rock_i-1]), eval(rock_lines[rock_i]))
        rock_positions = set(rock_positions)
    x_rocks, y_rocks = zip(*rock_positions)
    lower_boundary = max(y_rocks)

    # Simulate falling sand
    if part == 1:
        return simulate_sand_part1(rock_positions, start_pos, lower_boundary)
    elif part == 2:
        # Add a floor
        increase = 100
        rock_positions = rock_positions | {(i, lower_boundary+2) for i in range(min(x_rocks)-increase, max(x_rocks)+increase+1)}    
        return simulate_sand_part2(rock_positions, start_pos, lower_boundary, [min(x_rocks)-increase, max(x_rocks)+increase])

        


        


if __name__ == "__main__":
    filepath="data/day14.txt"
    # filepath="data/test_day14.txt"

    print(f"Number of sand units until it falls in the abyss: {simulate_sand(filepath, part=1)}")
    print(f"Number of sand units until it blocks: {simulate_sand(filepath, part=2)}")