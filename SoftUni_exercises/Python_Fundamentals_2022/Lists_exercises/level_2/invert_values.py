numbers = input()
split_numbers = numbers.split()
new_list = []
for num in split_numbers:
	if int(num) > 0:
		new_list.append(-abs(int(num)))
	else:
		new_list.append(abs(int(num)))
print(new_list)

#second easier method:

# list_of_numbers = input().split()
# opposite_numbers = []
# for element in list_of_numbers:
# 	current_number = -int(element)
# 	opposite_numbers.append(element)
# print(opposite_numbers)