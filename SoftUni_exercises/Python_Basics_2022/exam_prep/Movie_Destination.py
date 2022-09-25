budget_for_the_movie = float(input())
destination = input()
season = input()
number_of_days = int(input())

if destination == "Dubai":
    if season == "Winter":
        number_of_days *= 45000
    elif season == "Summer":
        number_of_days *= 40000

elif destination == "Sofia":
    if season == "Winter":
        number_of_days *= 17000
    elif season == "Summer":
        number_of_days *= 12500

elif destination == "London":
    if season == "Winter":
        number_of_days *= 24000
    elif season == "Summer":
        number_of_days *= 20250

total_price = number_of_days

if destination == "Dubai":
    total_price -= total_price * 0.3
elif destination == "Sofia":
    total_price += total_price * 0.25

if budget_for_the_movie >= total_price:
    print(f"The budget for the movie is enough! "
          f"We have {budget_for_the_movie - total_price:0.2f} leva left!")
else:
    print(f"The director needs {total_price - budget_for_the_movie:0.2f} leva more!")
