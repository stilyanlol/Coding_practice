n = int(input())
m = int(input())
s = int(input())

for a in range(m, n, -1):
    if a % 2 == 0 and a % 3 == 0:
        if a == s:
            break
        print(a, end=" ")