from algorithms.union_find.quick_find import QuickFind
from algorithms.union_find.quick_union import QuickUnion


def test_quick_find():
    algorithm = QuickFind(list(range(0, 10)))

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

    assert algorithm.connected(0, 1)


def test_quick_union():
    algorithm = QuickUnion(list(range(0, 10)))

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

    assert algorithm.connected(0, 1)
