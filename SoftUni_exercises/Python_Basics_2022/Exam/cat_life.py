cats_breed = input()
cats_sex = input()

years = 0

if cats_breed == "British Shorthair":
    if cats_sex == "m":
        years = 13
    elif cats_sex == "f":
        years = 14

elif cats_breed == "Siamese":
    if cats_sex == "m":
        years = 15
    elif cats_sex == "f":
        years = 16

elif cats_breed == "Persian":
    if cats_sex == "m":
        years = 14
    elif cats_sex == "f":
        years = 15

elif cats_breed == "Ragdoll":
    if cats_sex == "m":
        years = 16
    elif cats_sex == "f":
        years = 17

elif cats_breed == "American Shorthair":
    if cats_sex == "m":
        years = 12
    elif cats_sex == "f":
        years = 13

elif cats_breed == "Siberian":
    if cats_sex == "m":
        years = 11
    elif cats_sex == "f":
        years = 12

else:
    print(f"{cats_breed} is invalid cat!")

human_months = years * 12
cat_months = human_months / 6

print(f"{round(cat_months)} cat months")
