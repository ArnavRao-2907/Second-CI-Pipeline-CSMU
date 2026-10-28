def mz(values, size):
	"""Move zeroes to the end without using list methods or helper functions."""
	next_position = 0
	index = 0

	while index < size:
		if values[index] != 0:
			values[next_position] = values[index]
			next_position += 1
		index += 1

	while next_position < size:
		values[next_position] = 0
		next_position += 1

	return values


print(mz([0], 1))