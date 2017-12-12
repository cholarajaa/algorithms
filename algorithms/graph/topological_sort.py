def matrix_graph(graph):
    linear_order = []
    in_degree = [0] * len(graph)

    for vertex, adjacents in enumerate(graph):
        for adjacent_vertex, is_adjacent in enumerate(adjacents):
            in_degree[adjacent_vertex] += is_adjacent

    zero_in_degree = [vertex for vertex, adjacents in enumerate(in_degree) if adjacents == 0]

    while zero_in_degree:
        vertex = zero_in_degree.pop(0)
        linear_order.append(vertex)

        for adjacent_vertex, is_adjacent in enumerate(graph[vertex]):
            if not is_adjacent:
                continue

            in_degree[adjacent_vertex] -= 1
            if in_degree[adjacent_vertex] == 0:
                zero_in_degree.append(adjacent_vertex)

    return linear_order


def adjacent_list(graph):
    linear_order = []
    in_degree = [0] * len(graph)

    for vertex, adjacents in enumerate(graph):
        for adjacent_vertex in adjacents:
            in_degree[adjacent_vertex] += 1

    zero_in_degree = [vertex for vertex, adjacents in enumerate(in_degree) if adjacents == 0]

    while zero_in_degree:
        vertex = zero_in_degree.pop(0)
        linear_order.append(vertex)

        for adjacent_vertex in graph[vertex]:
            in_degree[adjacent_vertex] -= 1

            if in_degree[adjacent_vertex] == 0:
                zero_in_degree.append(adjacent_vertex)

    return linear_order


def graph_dict(graph):
    linear_order = []
    in_degree = {vertex: 0 for vertex in graph}

    for vertex, adjacents in graph.items():
        for adjacent_vertex in adjacents:
            in_degree[adjacent_vertex] = in_degree.get(adjacent_vertex, 0) + 1

    zero_in_degree = [vertex for vertex in in_degree if in_degree[vertex] == 0]

    while zero_in_degree:
        vertex = zero_in_degree.pop(0)
        linear_order.append(vertex)

        for adjacent_vertex in graph[vertex]:
            in_degree[adjacent_vertex] -= 1

            if in_degree[adjacent_vertex] == 0:
                zero_in_degree.append(adjacent_vertex)

    return linear_order
