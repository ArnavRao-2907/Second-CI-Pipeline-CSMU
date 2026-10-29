def mf(values):
	"""Print and return the most frequent value; ties go to the first value."""
	if values is None:
		return None

	most_frequent = None
	highest_count = 0
	index = 0

	while index < len(values):
		current_count = 0
		scan_index = 0

		while scan_index < len(values):
			if values[scan_index] == values[index]:
				current_count += 1
			scan_index += 1

		if current_count > highest_count:
			highest_count = current_count
			most_frequent = values[index]

		index += 1

	return most_frequent

print(mf([9]))