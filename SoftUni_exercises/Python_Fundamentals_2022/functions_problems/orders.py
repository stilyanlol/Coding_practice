def orders(item, quantity):
    if item == 'coffee':
        total = 1.5 * quantity 
    elif item == 'coke':
        total = 1.4 * quantity
    elif item == 'water':
        total = 1.0 * quantity
    elif item == 'snacks':
        total = 2.0 * quantity

    return total


product = input()
quantitie = int(input())
print(f'{orders(product, quantitie):.2f}')