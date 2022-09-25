from sys import maxsize

n = int(input())
min_num = maxsize

while True:

    current_num = int(input())

    if current_num < min_num:
        print(current_num)

    current_num = input()

    if current_num == "Stop":
        break
