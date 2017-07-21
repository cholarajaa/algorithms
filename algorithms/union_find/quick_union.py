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
