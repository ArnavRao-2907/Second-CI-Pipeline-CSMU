def tm(matrix):
	"""Print and return the transpose of a rectangular matrix."""
	if not matrix:
		print("[]")
		return []

	rows = len(matrix)
	columns = len(matrix[0])

	for row in matrix:
		if len(row) != columns:
			raise ValueError("The matrix must be rectangular.")

	transposed = []
	for column_index in range(columns):
		new_row = []
		for row_index in range(rows):
			new_row.append(matrix[row_index][column_index])
		transposed.append(new_row)

	# Display each row in matrix form without using a transpose helper.
	print("[")
	for row in transposed:
		line = " ["
		for index in range(len(row)):
			line += str(row[index])
			if index < len(row) - 1:
				line += ", "
		line += "]"
		print(line)
	print("]")

	return transposed


if __name__ == "__main__":
	tm([ ])
