"""
an aggregate of various helper functions made available for import
"""


def with_previous(iterable) -> tuple:
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


if __name__ == '__main__':
    for n in count(step=3):
        print(n)
        if n >= 15:
            break
