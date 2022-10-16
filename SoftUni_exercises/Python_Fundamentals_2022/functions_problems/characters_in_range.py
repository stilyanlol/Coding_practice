def characterize(a, b):
    ord_a = ord(a)
    ord_b = ord(b)

    lis = []

    for ch in range(ord_a, ord_b + 1):
        lis.append(chr(ch))

    return ' '.join(lis[1:-1])


a = input()
b = input()    
print(characterize(a, b))