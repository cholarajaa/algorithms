"""
    Test Topological Sort algorithm.

    Dependencies:

        Undershorts > Compression shorts > (Hose, Cup) > Pants (*Sweater) > Skates > Leg pades
        Socks > *Hose
        T-shirt > Chest pades > Sweater > Mask > Catch glove > Blocker

    Problem:
        I can't wear my Socks after the Hose, I can't wear my Hose before my Compression shorts...


    Map:
        0 - Undershorts
        1 - Socks
        2 - Compression shorts
        3 - Hose
        4 - Cup
        5 - Pants
        6 - Skates
        7 - Leg pades
        8 - T-shirt
        9 - Chest pades
        10 - Sweater
        11 - Mask
        12 - Catch glove
        13 - Blocker
"""
from algorithms.graph import topological_sort


items_map = {
    'undershorts': 0,
    'socks': 1,
    'compression_shorts': 2,
    'hose': 3,
    'cup': 4,
    'pants': 5,
    'skates': 6,
    'leg_pades': 7,
    't_shirt': 8,
    'chest_pade': 9,
    'sweater': 10,
    'mask': 11,
    'catch_glove': 12,
    'blocker': 13,
}

matrix_graph = [
    [0] * len(items_map.keys()) for i in range(0, len(items_map.keys()))
]
matrix_graph[items_map['undershorts']][items_map['compression_shorts']] = 1
matrix_graph[items_map['compression_shorts']][items_map['hose']] = 1
matrix_graph[items_map['compression_shorts']][items_map['cup']] = 1
matrix_graph[items_map['hose']][items_map['pants']] = 1
matrix_graph[items_map['cup']][items_map['pants']] = 1
matrix_graph[items_map['pants']][items_map['skates']] = 1
matrix_graph[items_map['skates']][items_map['leg_pades']] = 1
matrix_graph[items_map['leg_pades']][items_map['catch_glove']] = 1
matrix_graph[items_map['socks']][items_map['hose']] = 1
matrix_graph[items_map['pants']][items_map['sweater']] = 1
matrix_graph[items_map['t_shirt']][items_map['chest_pade']] = 1
matrix_graph[items_map['chest_pade']][items_map['sweater']] = 1
matrix_graph[items_map['sweater']][items_map['mask']] = 1
matrix_graph[items_map['mask']][items_map['catch_glove']] = 1
matrix_graph[items_map['catch_glove']][items_map['blocker']] = 1


adjacent_list_graph = [
    [items_map['compression_shorts']],
    [items_map['hose']],
    [items_map['hose'], items_map['cup']],
    [items_map['pants']],
    [items_map['pants']],
    [items_map['skates'], items_map['sweater']],
    [items_map['leg_pades']],
    [items_map['catch_glove']],
    [items_map['chest_pade']],
    [items_map['sweater']],
    [items_map['mask']],
    [items_map['catch_glove']],
    [items_map['blocker']],
    [],
]

graph_dict = {
    'undershorts': ['compression_shorts'],
    'socks': ['hose'],
    'compression_shorts': ['hose', 'cup'],
    'hose': ['pants'],
    'cup': ['pants'],
    'pants': ['skates', 'sweater'],
    'skates': ['leg_pades'],
    'leg_pades': ['catch_glove'],
    't_shirt': ['chest_pade'],
    'chest_pade': ['sweater'],
    'sweater': ['mask'],
    'mask': ['catch_glove'],
    'catch_glove': ['blocker'],
    'blocker': [],
}


def test_topological_sort_with_matrix_graph():
    results = topological_sort.matrix_graph(matrix_graph)
    assert results == [0, 1, 8, 2, 9, 3, 4, 5, 6, 10, 7, 11, 12, 13]


def test_topological_sort_with_adjacent_list_graph():
    results = topological_sort.adjacent_list(adjacent_list_graph)
    assert results == [0, 1, 8, 2, 9, 3, 4, 5, 6, 10, 7, 11, 12, 13]


def test_topological_sort_with_dict_graph():
    order = topological_sort.graph_dict(graph_dict)

    results = [items_map[vertex] for vertex in order]
    assert results == [0, 1, 8, 2, 9, 3, 4, 5, 6, 10, 7, 11, 12, 13]
