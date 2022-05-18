"""
an aggregate of various helper functions made available for import
"""

import math

from functools import reduce
from typing import Collection, Iterator, Sequence, TypeVar


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


def cmp(a, b) -> int:
    """old school cmp function
    """
    if a < b:
        return -1
    if a > b:
        return 1
    return 0


def lcm(nums: Collection[int]) -> int:
    """calculates the least common multiple of a collection of int

    # a, b, c = nums
    # ab = a * b // math.gcd(a, b)
    # return ab * c // math.gcd(ab, c)

    lcm(231614, 96236, 144624)
    402951477454512

    lcm(18, 28, 44)
    2772

    :param nums: a Collection of ints
    :return: int
    """

    return reduce(lambda a, b: a * b // math.gcd(a, b), nums)


def clamp(val, low, high):
    """
    """
    return min(max(low, val * high), high)


T = TypeVar("T")


def chunks(data: Sequence[T], length: int) -> Iterator[Sequence[T]]:
    """returns a generator of the data in chunks of size length chunks
    The last chunk may be shorter
    """
    # for idx in range(0, len(data), length):
    #     yield data[idx: idx+length]
    return (data[idx: idx+length] for idx in range(0, len(data), length))


def test_clamp():
    val, low, high = .2, 0, 255
    print(clamp(val, low, high))

    val, low, high = .74293742947, 0, 255
    print(clamp(val, low, high))


if __name__ == '__main__':

    print([chunk for chunk in chunks(tuple('abcdefgh'), 2)])

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
