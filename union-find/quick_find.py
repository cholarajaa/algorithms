# coding: utf-8


class QuickFind:
    """Quick find algorithm implementation."""

    def __init__(self, items):
        """Receive items and assign it to a self attribute."""
        self.items = items

    def connected(self, first_item, second_item):
        """Check if two components are connected."""
        return self.items[first_item] == self.items[second_item]

    def union(self, first_item, second_item):
        """Connect two components."""
        first_item_base = self.items[first_item]
        second_item_base = self.items[second_item]

        for index, item in enumerate(self.items):
            if item == first_item_base:
                self.items[index] = second_item_base


if __name__ == '__main__':
    algorithm = QuickFind(range(0, 10))

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
