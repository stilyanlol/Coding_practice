budget = float(input())
number_of_nights = int(input())
price_of_night = float(input())
additional_spending_percent = int(input())

if number_of_nights > 7:
    price_of_night -= price_of_night * 0.05

costs = price_of_night * number_of_nights
additional_spending_percent = budget * (additional_spending_percent / 100)
total_sum = costs + additional_spending_percent

if budget >= total_sum:
    print(f"Ivanovi will be left with {budget - total_sum:0.2f} leva after vacation.")
else:
    print(f"{total_sum - budget:0.2f} leva needed.")
