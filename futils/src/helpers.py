"""
an aggregate of various helper functions made available for import
"""

from typing import Iterator


def with_previous(iterable) -> Iterator:
    """returns an iterator of tuples (previous, current) items
    enumerated from the provided iterable parameter
    """
    def it():
        iterator = iter(iterable)
        previous = next(iterator)
        for current in iterator:
            yield previous, current
            previous = current
    return iter(it())


def count(start=0, step=1):
    """perpetual counter that starts at start, and increments by step
    generates an infinite sequence of numbers
    Make an iterator that returns consecutive integers starting with start.
    If not specified n defaults to zero. Often used as an argument to map()
    to generate consecutive data points.
    Also, used with zip() to add sequence numbers
    """
    n = 0
    while True:
        yield start + step * n
        n += 1


def transpose(iterable):
    return list(zip(*iterable))


def make_average():
    """ makes and returns a closure that can be incrementally called with
    the values to average, maybe as they become available, and returns their
    average calculated in a numerically stable manner

    :return: a closure

    >>> avg = make_average()
    >>> print(avg(10))
    10.0
    >>> print(avg(11))
    10.5
    >>> print(avg(12))
    11.0
    >>> print(avg(13))
    11.5
    """
    total = 0
    num_val = 0
    def averager(new_val):
        nonlocal total, num_val
        total += new_val
        num_val += 1
        return total / num_val
    return averager


def clamp(val, low, high):
    """
    """
    return min(max(low, val * high), high)


def test_clamp():
    val, low, high = .2, 0, 255
    print(clamp(val, low, high))

    val, low, high = .74293742947, 0, 255
    print(clamp(val, low, high))


if __name__ == '__main__':
    test_clamp()

    print()

    for n in count(step=3):
        print(n)
        if n >= 15:
            break

    avg = make_average()

    print(avg(10))
    print(avg(11))
    print(avg(12))
    print(avg(13))

    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(avg.__closure__[0].cell_contents)
