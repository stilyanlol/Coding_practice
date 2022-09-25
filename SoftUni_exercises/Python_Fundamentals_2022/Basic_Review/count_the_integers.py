numbers = input()

count = 0

while numbers.isdigit():
    if len(numbers) > 7:
        break
    count += 1
    numbers = input()

print(count)
