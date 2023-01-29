n = 3
m = 3
val = [0] * n
for x in range (n):
    val[x] = [0] * m
print(val)


val = [['Dave',101,90,95], \
       ['Alex',102,85,100], \
       ['Ray',103,90,95]]

print(val[2])

print(val[0][1])

val = [['Dave',101,90,95], ['Alex',102,85,100], ['Ray',103,90,95]]

print(val[-2])

print(val[-1][-2])