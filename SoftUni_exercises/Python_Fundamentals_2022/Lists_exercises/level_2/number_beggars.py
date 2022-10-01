numbers = input().split(', ')
count_of_beggars = int(input())

output_sum = []
numbers_list_as_digits = []
starting_index = 0

for element in numbers:
    numbers_list_as_digits.append(int(element))

while starting_index < count_of_beggars:
    sum_for_current_beggar = 0

    for current_index in range(starting_index, len(numbers_list_as_digits), count_of_beggars):
        sum_for_current_beggar += numbers_list_as_digits[current_index]

    output_sum.append(sum_for_current_beggar)
    starting_index += 1

print(output_sum)
