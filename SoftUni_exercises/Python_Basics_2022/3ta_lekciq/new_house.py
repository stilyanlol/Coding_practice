type_of_flower = input()
number_of_flowers = int(input())
budget = int(input())

total = 0
discount = 0
total_with_discount = 0

if type_of_flower == "Roses":
    total = number_of_flowers * 5
    if number_of_flowers > 80:
        discount = 0.1 * total
        total_with_discount = total - discount
elif type_of_flower == "Dahlias":
    total = number_of_flowers * 3.80
    if number_of_flowers > 90:
        discount = 0.15 * total
        total_with_discount = total - discount
elif type_of_flower == "Tulips":
    total = number_of_flowers * 2.80
    if number_of_flowers > 80:
        discount = 0.15 * total
        total_with_discount = total - discount
elif type_of_flower == "Narcissus":
    total = number_of_flowers * 3
    if number_of_flowers < 120:
        discount = 0.15 * total
        total_with_discount = total - discount
elif type_of_flower == "Gladiolus":
    total = number_of_flowers * 2.50
    if number_of_flowers < 80:
        discount = 0.2 * total
        total_with_discount = total - discount

if budget >= total:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and "
          f"{'%0.2f' % (budget - total)} leva left.")
elif budget < total:
    print(f"Not enough money, you need {'%0.2f.' % (total - budget)} leva more.")

elif budget >= total_with_discount:
        print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and "
              f"{'%0.2f' % (budget - total_with_discount)} leva left.")
elif budget < total_with_discount:
        print(f"Not enough money, you need {'%0.2f.' % (total_with_discount - budget)} leva more.")
