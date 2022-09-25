kilos_bought_food = int(input())

total_food_eaten_by_puppy = 0
kilos_bought_food *= 1000

while True:

    food_eaten_by_puppy = input()

    total_food_eaten_by_puppy += int(food_eaten_by_puppy)


    if total_food_eaten_by_puppy <= kilos_bought_food:
        print(f"Food is enough! Leftovers: {kilos_bought_food - int(food_eaten_by_puppy)}"
              f" grams.")


    if total_food_eaten_by_puppy > kilos_bought_food:
        print(f"Food is not enough. You need {total_food_eaten_by_puppy - kilos_bought_food} grams more.")

    if food_eaten_by_puppy == "Adopted":
        break
