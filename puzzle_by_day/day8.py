# Lin Wouters
# 05-01-2023

import numpy as np

def visible_direction(trees, visible, index_range_i, index_range_j, max_tree=-1):
    for i in index_range_i:
        max_tree = -1
        for j in index_range_j:
            if trees[i][j] > max_tree:
                max_tree = trees[i][j]
                visible[i][j] += 1

    for j in index_range_j:
        max_tree = -1
        for i in index_range_i:
            if trees[i][j] > max_tree:
                max_tree = trees[i][j]
                visible[i][j] += 1

    return visible

def find_visible_trees(filepath):
    """Return the number of trees visible"""
    with open(filepath) as f:
        file = f.read()
        trees = np.array([[int(i) for i in list(line)] for line in file.split()])
    visible = np.zeros(trees.shape)

    # From both up and down, go look in the row and column
    visible = visible_direction(trees, visible, range(trees.shape[0]), range(trees.shape[1]), max_tree=-1)
    visible = visible_direction(trees, visible, range(trees.shape[0]-1, -1, -1), range(trees.shape[1]-1, -1, -1), max_tree=-1)

    return np.count_nonzero(visible)

### PART 2 ###

def scenic_score_row(trees, i, j, score, tree_range):
    # Look in the row
    visible = 0
    for see_j in tree_range:
        # Add a tree
        visible += 1
        # If the tree is same height or higher, the rest is not visible
        if trees[i][see_j] >= trees[i][j]:
            break

    return score * visible

def scenic_score_col(trees, i, j, score, tree_range):
    # Look in the column
    visible = 0
    for see_i in tree_range:
        # Add a tree
        visible += 1
        # If the tree is same height or higher, the rest is not visible
        if trees[see_i][j] >= trees[i][j]:
            break

    return score * visible

def scenic_score(trees, i, j):
    # The score is 0 if the tree is at an edge
    if i == 0 or j == 0 or i == trees.shape[0]-1 or j == trees.shape[1]-1:
        return 0

    score = 1
    # Look in the columns
    score = scenic_score_col(trees, i, j, score, range(i+1, trees.shape[0]))
    score = scenic_score_col(trees, i, j, score, range(i-1, -1, -1))
    # Look in the rows
    score = scenic_score_row(trees, i, j, score, range(j+1, trees.shape[1]))
    score = scenic_score_row(trees, i, j, score, range(j-1, -1, -1))

    return score


def best_scenic_score(filepath):
    """Return the scenic score of the best tree"""

    with open(filepath) as f:
        file = f.read()
        trees = np.array([[int(i) for i in list(line)] for line in file.split()])
    
    # For each tree, find scenic score
    best_score = 0
    for i in range(trees.shape[0]):
        for j in range(trees.shape[1]):
            best_score = max(best_score, scenic_score(trees, i, j))

    return best_score


if __name__ == "__main__":
    filepath="data/day8.txt"
    # filepath="data/test_day8.txt"

    print(f"The number of visible trees is: {find_visible_trees(filepath)}")
    print(f"The scenic score of the best tree is: {best_scenic_score(filepath)}")