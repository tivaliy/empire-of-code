from operator import itemgetter
from string import ascii_lowercase
import itertools


def most_letter(text, all_letters=False):
    val = [(ascii_lowercase[i], v) for i, v in
           enumerate(map(lambda x: text.lower().count(x), ascii_lowercase))]
    k = (filter(lambda x: x[1], sorted(val, key=itemgetter(1))))
    l = ["".join(char for char, num in tuples) for num, tuples
         in itertools.groupby(k, key=lambda a: a[1])]
    return l[-1][0] if not all_letters else ''.join([i for i in reversed(l)])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank_1
    assert most_letter("Hello World!") == "l", "Hello test"
    assert most_letter("How do you do?") == "o", "O is most wanted"
    result = most_letter("One")
    assert len(result) == 1 and result in "one", "All letter only once."
    assert most_letter("Oops!") == "o", "Don't forget about lower case."
    result = most_letter("AAaooo!!!!")
    assert len(result) == 1 and result in "ao", "Only letters."
    result = most_letter("abe")
    assert len(result) == 1 and result in "abe", "The First."
    result = most_letter("Lorem ipsum dolor sit amet")
    assert len(result) == 1 and result in "mo", "Lorem 1."

    # Rank_2
    assert most_letter("Lorem ipsum dolor sit amet") == "m", "Lorem 2."
    assert most_letter("One") == "e", "One 2"
    assert most_letter("AAaooo!!!!") == "a", "Only letters. 2"
    assert most_letter("bcdefghijklmnaopqrstuvwxyz") == "a", "ABC"

    # Rank_3
    assert most_letter("Lorem ipsum dolor sit amet", True) == "moeilrstadpu", "Lorem 3."

    print("Use 'Check' to earn sweet rewards!")
