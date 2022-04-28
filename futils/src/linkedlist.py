"""

llist([iterable]) returns a singly linked list

dlist([iterable]) returns a doubly linked list

internal nodes are called Records

"""

from dataclasses import dataclass


class llist:
    """
    a base singly linked list
    """

    @dataclass
    class _Record:
        item = None
        next = None

        def __repr__(self) -> str:
            return repr(self.item)

    def __init__(self) -> None:
        self.head: llist._Record or None = None
        self.tail: llist._Record or None = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def __bool__(self) -> bool:
        return bool(len(self))

    def __str__(self) -> str:
        res = ['< '] if self else ['<']
        res += ' -> '.join([repr(record.item) for record in self])
        res += [' >'] if self else ['>']
        return ''.join(res)

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur
            cur = cur.next

    def add_first(self, item) -> None:
        """adds an item at the head of the llist

        item: the item to be added
        """
        record = self._Record()
        record.item = item
        record.next = self.head
        self.head = record
        if len(self) == 1:
            self.tail = self.head.next
        self._size += 1

    def add_last(self, item) -> None:
        """adds an item at the tail of the llist

        item: the item to be added
        """
        record = self._Record()
        record.item = item
        if len(self) == 0:
            record.next = self.head
            self.head = record
        elif len(self) == 1:
            self.tail = record
            self.head.next = self.tail
        else:
            self.tail.next = record
            self.tail = record
        self._size += 1


if __name__ == '__main__':

    linseq = llist()
    print(len(linseq), linseq)

    linseq.add_first('A')
    print(len(linseq), linseq)

    linseq.add_first('B')
    print(len(linseq), linseq)

    linseq.add_first('C')
    print(len(linseq), linseq)

    linseq.add_last('A')
    print(len(linseq), linseq)

    linseq.add_last('B')
    print(len(linseq), linseq)

    linseq.add_last('C')
    print(len(linseq), linseq)

    del linseq
    print('-' * 100)

    linseq = llist()
    print(len(linseq), linseq)

    linseq.add_last('A')
    print(len(linseq), linseq)

    linseq.add_last('B')
    print(len(linseq), linseq)

    linseq.add_last('C')
    print(len(linseq), linseq)

    linseq.add_first('A')
    print(len(linseq), linseq)

    linseq.add_first('B')
    print(len(linseq), linseq)

    linseq.add_first('C')
    print(len(linseq), linseq)

    print('done!')
