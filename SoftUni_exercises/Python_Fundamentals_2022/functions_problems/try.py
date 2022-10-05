lst = [12, 50, 13, 50, 1, 4]
mx = max(lst)
m = [i for i, j in enumerate(lst) if j == mx]
print(m[-1])