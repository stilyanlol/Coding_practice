#list comprehension
result = [int(x) for x in input().split(' ') if int(x) % 2 == 0]
print(result)


#filter
# number = input().split(' ')
# result = filter(lambda x: int(x) % 2 == 0, number)
# print(list(result))