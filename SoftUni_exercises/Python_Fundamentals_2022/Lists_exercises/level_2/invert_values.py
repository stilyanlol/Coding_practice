numbers = input()
split_numbers = numbers.split()
new_list = []

for num in split_numbers:

	if int(num) > 0:
		new_list.append(-abs(int(num)))
	else:
		new_list.append(abs(int(num)))

print(new_list)