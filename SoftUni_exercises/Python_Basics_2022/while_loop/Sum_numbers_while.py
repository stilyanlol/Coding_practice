const_num = int(input())
sum_nums = 0

while True:

    current_num = int(input())
    sum_nums += current_num

    if sum_nums >= const_num:
        print(sum_nums)
        break
