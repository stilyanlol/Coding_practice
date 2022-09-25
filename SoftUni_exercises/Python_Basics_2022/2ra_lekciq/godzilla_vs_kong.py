budget = float(input())
statists = int(input())
price_of_clothing = float(input())

decoration = 0.1 * budget
price_of_clothing *= statists

if statists > 150:
    price_of_clothing = price_of_clothing - (0.1 * price_of_clothing)

if decoration + price_of_clothing > budget:
    print("Not enough money!")
    print(f"Wingard needs {'%0.2f' % ((decoration + price_of_clothing) - budget)} leva more.")

if decoration + price_of_clothing <= budget:
    print("Action!")
    print(f"Wingard starts filming with {'%0.2f' % (budget - (decoration + price_of_clothing))} leva left.")
