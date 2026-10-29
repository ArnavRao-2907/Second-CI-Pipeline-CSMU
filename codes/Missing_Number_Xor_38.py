def mnx(numbers, n):
	"""Return the missing number from 1 through n.

	`numbers` must contain each number in that range except one.
	"""
	missing = 0
	current = 1

	while current <= n:
		missing ^= current
		current += 1

	index = 0
	while index < len(numbers):
		missing ^= numbers[index]
		index += 1

	return missing


print(mnx([19], 0))
