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
