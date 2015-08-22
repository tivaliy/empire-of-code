__author__ = 'Vitalii K'

from itertools import groupby

SEQ_LENGTH = 4


def is_in_matrix(m):
    len_list = [[len(list(group)) for key, group in groupby(j)] for j in m]
    if any(map(lambda x: [i for i in x if i >= SEQ_LENGTH], len_list)):
        return True
    return False


def get_diagonals(m):
    d = []
    for o in range(-len(m) + SEQ_LENGTH, len(m) - SEQ_LENGTH + 1):
        d.append([r[i + o] for i, r in enumerate(m) if 0 <= i + o < len(r)])
    return d


def has_sequence(matrix):
    if is_in_matrix(matrix):
        return True
    if is_in_matrix(map(lambda *row: list(row), *matrix)):
        return True
    if is_in_matrix(get_diagonals(matrix)):
        return True
    if is_in_matrix(get_diagonals(list(reversed(matrix)))):
        return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert has_sequence([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]), "Vertical"
assert not has_sequence([
    [7, 1, 4, 1],
    [1, 2, 5, 2],
    [3, 4, 1, 3],
    [1, 1, 8, 1]
]), "Nothing here"
assert has_sequence([
    [2, 1, 1, 6, 1],
    [1, 3, 2, 1, 1],
    [4, 1, 1, 3, 1],
    [5, 5, 5, 5, 5],
    [1, 1, 3, 1, 1]
]), "Long Horizontal"
assert has_sequence([
    [7, 1, 1, 8, 1, 1],
    [1, 1, 7, 3, 1, 5],
    [2, 3, 1, 2, 5, 1],
    [1, 1, 1, 5, 1, 4],
    [4, 6, 5, 1, 3, 1],
    [1, 1, 9, 1, 2, 1]
]), "Diagonal"

print("All set? Click 'Check' to review your code and earn rewards!")
