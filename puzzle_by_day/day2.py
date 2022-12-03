# AOC 2022-12-02
# Lin Wouters

def get_score_part1(opponent, yourself):
    """
    Return the score for a single round, based on the opponents shape, and
    your own shape.
    The score is score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
    Where rock=1, paper=2 and scissors=3
    """
    # TODO: use modulo?
    # draw
    if yourself == opponent:
        return 3 + int(yourself)
    # win
    elif ((yourself == '1' and opponent == '3') or
        (yourself == '2' and opponent == '1') or
        (yourself == '3' and opponent == '2')):
        return 6 + int(yourself)
    # lose
    else:
        return int(yourself)
    

def get_score_part2(opponent, result):
    """
    Return the score for a single round, based on the opponents shape, and
    the result of the game (win, lose, draw)
    The score is score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
    Where rock=1, paper=2 and scissors=3,
    lose=1, draw=2, win=3.
    """
    # draw
    if result == '2':
        return 3 + int(opponent)
    # win
    elif result == '3':
        if opponent == '1':
            return 6 + 2
        elif opponent == '2':
            return 6 + 3
        elif opponent == '3':
            return 6 + 1
    # lose
    elif result == '1':
        if opponent == '1':
            return 3
        elif opponent == '2':
            return 1
        elif opponent == '3':
            return 2


def get_scores(filepath):
    """
    Return the scores when following the strategy path
    """

    replace_dict = {'A': '1', 'B':'2', 'C':'3', 'X':'1', 'Y':'2', 'Z':'3'}
    with open(filepath) as f:
        file = f.read()
        # Replace letters by their score
        for letter, number in replace_dict.items():
            file = file.replace(letter, number).strip()
        # Add the score per round
        score_1 = 0
        score_2 = 0
        for play in file.split('\n'):
            opponent, yourself = play.split(' ')
            score_1 += get_score_part1(opponent, yourself)
            score_2 += get_score_part2(opponent, yourself)

    return score_1, score_2


if __name__ == "__main__":
    filepath="../data/day2.txt"
    score_1, score_2 = get_scores(filepath)
    print(f"The total score if everything goes right with the second column being your own shape would be: {score_1}")
    print(f"The total score if everything goes right with the second column being the result would be: {score_2}")