from functools import reduce


def count_chars(s):
    return (reduce(lambda x, y: x + y.isalpha(), s, 0), reduce(lambda x, y: x + y.isdigit(), s, 0), reduce(lambda x, y: x + (not(y.isalnum())), s, 0))