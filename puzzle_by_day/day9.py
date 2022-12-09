# AOC 2022-12-09
# Lin Wouters

import numpy as np

class long_rope_grid:
    def __init__(self, num_knots):
        self.num_knots = num_knots
        self.knot_positions = np.zeros((num_knots, 2))
        self.positions_tail = [(0,0)] # Starting position

    def move(self, direction, times):
        for i in range(times):
            # Move head
            self.move_head(direction)
            # Move each of the following knots
            for knot_i in range(1, self.num_knots):
                self.move_tail(knot_i)
            # Save tails position
            self.positions_tail.append(tuple(self.knot_positions[-1]))

    def move_head(self, direction):
        # Move head one step into the direction
        if direction == 'U':
            self.knot_positions[0][1] += 1
        elif direction == 'D':
            self.knot_positions[0][1] -= 1
        elif direction == 'R':
            self.knot_positions[0][0] += 1
        elif direction == 'L':
            self.knot_positions[0][0] -= 1

    def move_tail(self, knot_i):
        # If not touching, move tail in the direction of the knot before it
        if (abs(self.knot_positions[knot_i-1][0]-self.knot_positions[knot_i][0]) > 1 
                or abs(self.knot_positions[knot_i-1][1]-self.knot_positions[knot_i][1]) > 1):
            self.knot_positions[knot_i] += np.sign(self.knot_positions[knot_i-1]-self.knot_positions[knot_i])


def move_long_rope(filepath, num_knots):
    rope = long_rope_grid(num_knots)

    with open(filepath) as f:
        for line in f:
            # Move the rope
            direction, times = line.strip().split(' ')
            rope.move(direction, int(times))

    # Return the number of unique positions the tail has visited
    return len(set(rope.positions_tail))


if __name__ == "__main__":
    filepath="../data/day9.txt"
    # filepath="../data/test_day9.txt"
    print(f"The number of positions the tail visited with 2 knots is: {move_long_rope(filepath, 2)}")
    print(f"The number of positions the tail visited with 10 knots is: {move_long_rope(filepath, 10)}")
