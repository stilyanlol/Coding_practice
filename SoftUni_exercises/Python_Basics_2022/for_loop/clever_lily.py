n = int(input())

price_of_washingmaschine = float(input())
price_of_one_toy = int(input())

even_number_of_birthdays = 0
odd_number_of_birthdays = 0
total_money = 0
money_multiplier = 0

for i in range(1, n + 1):

    if i % 2 == 0:
        even_number_of_birthdays += 1
        money_multiplier += 1
        total_money += 10 * money_multiplier
    else:
        odd_number_of_birthdays += 1

total_money -= even_number_of_birthdays

total_money += price_of_one_toy * odd_number_of_birthdays

if total_money < price_of_washingmaschine:
    print(f"No! {price_of_washingmaschine - total_money:0.2f}")
else:
    print(f"Yes! {total_money - price_of_washingmaschine:0.2f}")
