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
