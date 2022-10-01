number = int(input())
lis = []
filtered_lis = []

for i in range(number):
    num = input()
    lis.append(num)

command = input()

if command == 'even':
    for j in lis:
        if int(j) % 2 == 0:
            filtered_lis.append(int(j))
if command == 'odd':
    for j in lis:
        if int(j) % 2 != 0:
            filtered_lis.append(int(j))
if command == 'positive':
    for j in lis:
        if int(j) >= 0:
            filtered_lis.append(int(j))
if command == 'negative':
    for j in lis:
        if int(j) < 0:
            filtered_lis.append(int(j))

print(filtered_lis)