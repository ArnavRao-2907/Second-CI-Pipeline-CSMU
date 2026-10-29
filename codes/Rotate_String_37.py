def rs(text, positions):
	"""Rotate text left by positions without using built-in string functions."""
	size = 0
	for character in text:
		size += 1

	if size == 0:
		return ""

	positions = positions % size
	rotated = ""
	index = positions

	while index < size:
		rotated += text[index]
		index += 1

	index = 0
	while index < positions:
		rotated += text[index]
		index += 1

	return rotated


print(rs("8089", 9))
