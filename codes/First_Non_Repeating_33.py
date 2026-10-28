def fnr(text):
	index = 0
	while index < len(text):
		character = text[index]
		occurrences = 0
		check_index = 0

		while check_index < len(text):
			if text[check_index] == character:
				occurrences += 1
			check_index += 1

		if occurrences == 1:
			return character
		index += 1

	return None


print(fnr(" "))
print(fnr(""))