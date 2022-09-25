number_of_days = int(input())
total_food = float(input())

total_food_dog = 0
total_food_cat = 0
biscuits = 0
total_food_eaten = 0

for days in range(1, number_of_days + 1):

    food_eaten_by_dog = int(input())
    food_eaten_by_cat = int(input())

    total_food_dog += food_eaten_by_dog
    total_food_cat += food_eaten_by_cat

    total_food_eaten = total_food_dog + total_food_cat

    if days % 3 == 0:
        biscuits += (food_eaten_by_dog + food_eaten_by_cat) / 10

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_food_eaten * (100 / total_food):0.2f}% of the food has been eaten.")
print(f"{total_food_dog * (100 / total_food_eaten):0.2f}% eaten from the dog.")
print(f"{total_food_cat * (100 / total_food_eaten):0.2f}% eaten from the cat.")
