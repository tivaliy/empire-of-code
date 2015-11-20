__author__ = 'Vitalii K'


def xo_referee(result):
    array = []
    # Add rows
    array.extend(result)
    # Add columns
    for j in range(len(result)):
        m = ''
        for i in range(len(result)):
            m += result[i][j]
        array.append(m)
    # Add main diagonals
    array.append(''.join([str(result[i][i]) for i in range(len(result[0]))]))
    array.append(''.join([str(result[len(result[0]) - 1 - i][i])
                          for i in range(len(result[0]) - 1, -1, -1)]))
    if any('XXX' in x for x in array) and any('OOO' in o for o in array):
        return 'D'
    for item in array:
        if 'XXX' in item:
            return 'X'
        if 'OOO' in item:
            return 'O'
    return 'D'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert xo_referee([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert xo_referee([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert xo_referee([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert xo_referee([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

    # Rank 2
    assert xo_referee([
        ".OX",
        ".OX",
        ".OX"]) == "D", "Mexican Vertical Duel"
    assert xo_referee([
        '.XO',
        'XXX',
        'OOO']) == "D", "Mexican Horizontal Duel"

    # Rank 3
    assert xo_referee([
        'XOO.',
        '.X.O',
        'X.OO',
        'XXOX']) == "D", "4WD"
    assert xo_referee([
        'XOO.',
        '.X.O',
        'XXOO',
        'XXOX']) == "X", "4X4"
    assert xo_referee(
        ['XOO.',
         '.XOO',
         'XXOO',
         'XXOX']) == "D"
