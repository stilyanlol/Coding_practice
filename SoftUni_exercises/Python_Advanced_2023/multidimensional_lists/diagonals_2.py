num = int(input())

matrix = [[int(el) for el in input().split(", ")] for _ in range(num)]

primary_diag = [matrix[r][r] for r in range(num)]
secondary_diag = [matrix[r][num - r - 1] for r in range(num - 1, -1, -1)]

print(*primary_diag, *secondary_diag, end=', ')