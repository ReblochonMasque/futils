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
    """
    ndx = start
    while True:
        yield start
        start += step


if __name__ == '__main__':
    for n in count(step=3):
        print(n)
        if n >= 15:
            break
