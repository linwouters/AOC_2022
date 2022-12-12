# Lin Wouters
# 12-12-2022

import numpy as np


def get_options(grid, pos, traversed):
    # Get possible neighbors
    options = []
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        # If the option is within bounds of the grid
        if (pos[0]+i) < 0 or (pos[1]+j) < 0  or (pos[0]+i) > (grid.shape[0]-1) or (pos[1]+j) > (grid.shape[1]-1):
            continue
        # Get the options that one can reach (i.e. not more than 1 value higher), and has not visited yet
        elif (grid[pos[0]+i][pos[1]+j] <= (grid[pos[0]][pos[1]] + 1)) and ((pos[0]+i, pos[1]+j) not in traversed):
            options.append((pos[0]+i, pos[1]+j))
    return options


def BFA(grid, start_pos, end_pos):
    # Perform BFA to find shortest path
    paths = [[start_pos]]
    visited = {start_pos}
    path_idx = 0

    while path_idx < len(paths):
        # Current path
        current_path = paths[path_idx]
        # Find possible neighbors
        neighbors = get_options(grid, current_path[-1], visited)
        for neigh in neighbors:
            # Return path if the end position is found
            if neigh == end_pos:
                # return current_path + [neigh]
                return len(current_path)
            if not neigh in visited:
                # Update paths to traverse with new neighbors
                paths.append(current_path + [neigh])
                visited.add(neigh)
        path_idx += 1

    return None


def find_shortest_path_a(grid, start_pos, end_pos):
    # Find all places with an a
    a_positions = list(zip(*np.where(grid==0)))
    path_lengths = []
    # Find the lengths for all possible starting places
    for a_pos in a_positions:
        path_lengths.append(BFA(grid, a_pos, end_pos))

    return path_lengths


def determine_shortest_path(filepath, part=1):
    with open(filepath) as f:
        file = f.read().split()
        # Cast all letters to numbers between 0-25
        grid = np.array([[ord(char)-97 for char in list(row)] for row in file])
        # Get start and end positoin
        start_pos = tuple(list(zip(*np.where(grid==-14)))[0])
        end_pos = tuple(list(zip(*np.where(grid==-28)))[0])
        # Replace start and end position with their height value
        grid[start_pos[0]][start_pos[1]] = 0
        grid[end_pos[0]][end_pos[1]] = 25
        if part == 1:
            # Perform BFA to find the shortest route
            shortest_path = BFA(grid, start_pos, end_pos)
            return shortest_path
        elif part == 2:
            # Find shortest route for all starting positions with elevation a
            path_lengths = find_shortest_path_a(grid, start_pos, end_pos)
            # Find shortest route of these possible routes
            return min([length for length in path_lengths if length != None])
        else:
            raise ValueError


if __name__ == "__main__":
    filepath="data/day12.txt"
    # filepath="data/test_day12.txt"

    print(f"Shortest path from your starting position is: {determine_shortest_path(filepath, part=1)}")
    print(f"Shortest path from any position at elevation a is: {determine_shortest_path(filepath, part=2)}")