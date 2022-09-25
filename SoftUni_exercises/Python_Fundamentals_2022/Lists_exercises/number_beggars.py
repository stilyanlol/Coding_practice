numbers = input()
count_of_beggars = int(input())

output_sum = []

for num in numbers.split(', '):
    for beggar in range(count_of_beggars):
        output_sum.append([int(num)])

print(f'This is the sum of the list {(output_sum)}')
