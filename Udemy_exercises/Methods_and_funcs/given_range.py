def ran_check(num,low,high):
    if num in range(low, high + 1):
        return f'{num} is in the range between {low} and {high}'

print(ran_check(4,3,9))