def linear_search(array, expected_item):
	result = -1

	for index, item in enumerate(array):
		if item == expected_item:
			result = index
	return result


def better_linear_search(array, expected_item):
	for index, item in enumerate(array):
		if item == expected_item:
			return index
	return -1


def sentinel_linear_search(array, expected_item):
	last_item = array[-1]
	array[-1] = expected_item

	i = 0
	while array[i] != expected_item:
		i += 1

	array[-1] = last_item

	if i + 1 < len(array) or array[-1] == expected_item:
		return i
	return -1