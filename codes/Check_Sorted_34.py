def cs(numbers):
	if numbers is None:
		return None

	iterator = iter(numbers)
	try:
		previous = next(iterator)
	except StopIteration:
		return None

	for current in iterator:
		if current < previous:
			return False
		previous = current

	return True

print(cs([9, 0, ]))