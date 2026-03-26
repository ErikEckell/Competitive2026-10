from sys import stdin

def read_input(lines):
	clean_lines = [line.strip() for line in lines if line.strip()]
	if not clean_lines:
		return

	index = 0
	total_cases = int(clean_lines[index])
	index += 1

	for _ in range(total_cases):
		digits_count = int(clean_lines[index])
		index += 1

		first_number_digits = []
		second_number_digits = []

		for _ in range(digits_count):
			first_digit, second_digit = clean_lines[index].split()
			first_number_digits.append(first_digit)
			second_number_digits.append(second_digit)
			index += 1

		yield digits_count, "".join(first_number_digits), "".join(second_number_digits)

for digits_count, first_number, second_number in read_input(stdin.readlines()):
    print(str(int(first_number) + int(second_number)) + "\n")
	




