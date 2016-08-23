"""Advanced skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    letters_count = {}

    for char in phrase.replace(" ", ""):

        if char not in letters_count:

            letters_count[char] = 1

        else:

            letters_count[char] += 1

    max_count = 0

    top_letters = []

    for letter in letters_count:

        if letters_count[letter] > max_count:

            max_count = letters_count[letter]

    for letter in letters_count:

        if letters_count[letter] == max_count:

            top_letters.append(letter)

    return top_letters


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    words_len = {}

    for word in words:

        length_word = len(word)

        if length_word not in words_len:

            words_len[length_word] = [word]

        else:

            words_len[length_word].append(word)

            words_len[length_word].sort()

    return words_len.items()

#####################################################################

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
