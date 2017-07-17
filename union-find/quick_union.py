# coding: utf-8


class QuickUnion:
    """Quick union algorithm implementation."""

    def __init__(self, items):
        self.items = items

    def find_root(self, index):
        """Find the root from index."""
        while (index != self.items[index]):
            index = self.items[index]
        return index

    def connected(self, first_item, second_item):
        """Verify if the components were connected."""
        return self.find_root(first_item) == self.find_root(second_item)

    def union(self, first_item, second_item):
        """Connect two components."""
        first_item_root = self.find_root(first_item)
        second_item_root = self.find_root(second_item)

        self.items[first_item_root] = second_item_root


if __name__ == '__main__':
    algorithm = QuickUnion(range(0, 10))

    algorithm.union(4, 3)
    algorithm.union(3, 8)
    algorithm.union(6, 5)
    algorithm.union(9, 4)
    algorithm.union(2, 1)

    assert algorithm.connected(8, 9)
    assert algorithm.connected(5, 4) is False

    algorithm.union(5, 0)
    algorithm.union(7, 2)
    algorithm.union(6, 1)
    algorithm.union(7, 3)

    print(algorithm.items)
