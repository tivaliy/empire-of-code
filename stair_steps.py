def checkio(n):
    o, t = 0, 0
    for n in n:
        t, o = o, max(o, t) + n
    return max(o, t)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert golf((5, -3, -1, 2)) == 6
    assert golf((5, 6, -10, -7, 4)) == 8
    assert golf((-11, 69, 77, -51, 23, 67, 35, 27, -25, 95)) == 393
    assert golf((-21, -23, -69, -67, 1, 41, 97, 49, 27)) == 125