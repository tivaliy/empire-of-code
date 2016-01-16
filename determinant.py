#!/usr/bin/env python
# -*- coding:utf8 -*-


def m(x, i, j):
    y = x[:]
    del (y[i - 1])
    y = list(zip(*y))
    del (y[j - 1])
    return list(zip(*y))


def golf(d):
    if len(d) == 1:
        return d[0][0]
    return sum([(-1) ** i * d[i][0] * golf(m(d, i + 1, 1))
                for i in range(len(d))])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert golf([[4, 3], [6, 3]]) == -6, 'First example'

    assert golf([[1, 3, 2],
                 [1, 1, 4],
                 [2, 2, 1]]) == 14, 'Second example'

