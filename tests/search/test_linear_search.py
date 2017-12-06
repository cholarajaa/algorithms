from algorithms.search import linear_search

import pytest


@pytest.mark.parametrize('algorithm', [
    linear_search.linear_search,
    linear_search.better_linear_search,
    linear_search.sentinel_linear_search
])
def test_algorithm_should_return_negative_index_when_not_found(algorithm):
    assert algorithm(list(range(0, 100000)), -2) == -1


@pytest.mark.parametrize('algorithm', [
    linear_search.linear_search,
    linear_search.better_linear_search,
    linear_search.sentinel_linear_search
])
def test_algorithm_should_return_index_from_element(algorithm):
    assert algorithm(list(range(0, 1000000)), 999999) == 999999