def ans(a, b):
	while b != 0:
		a, b = b, a % b

	if a < 0:
		a = -a
	return a


print(ans(2,127))