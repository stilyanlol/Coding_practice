lis = [12, 50, 13, 50, 1, 4]
for i in lis[::-1]:
    if i == max(lis):
        lis.remove(i)
        break
print(lis)