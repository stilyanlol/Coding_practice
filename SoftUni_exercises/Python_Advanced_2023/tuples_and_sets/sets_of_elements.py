length_1st, length_2nd = map(int, input().split())

set_1 = {int(input()) for _ in range(length_1st)}
set_2 = {int(input()) for _ in range(length_2nd)}

print(*set_1.intersection(set_2), sep="\n")