num = int(input())
word = input()

lis = []
filtered_lis = []

for w in range(num):
    sentence = input()
    lis.append(sentence)

print(lis)

for s in range(len(lis)-1, -1, -1):
    sentence_2 = lis[s]
    if word not in sentence_2:
        lis.remove(sentence_2)

print(lis)
