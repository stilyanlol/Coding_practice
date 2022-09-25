from sys import maxsize

n = int(input())

sum_of_nums = 0
max_num = -maxsize

for i in range(1, n + 1):

    num = int(input())

    sum_of_nums += num

    if num >= max_num:
        max_num = num

sum_of_nums -= max_num

if sum_of_nums == max_num:
    print(f"Yes \nSum = {max_num}")
else:
    print(f"No \nDiff = {abs(max_num - sum_of_nums)}")
