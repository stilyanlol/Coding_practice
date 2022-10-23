number_of_days = int(input())
number_of_players = int(input())
group_energy = float(input())
water_for_one_person = float(input())
food_for_one_person = float(input())

water_supply = number_of_players * number_of_days * water_for_one_person
food_supply = number_of_players * number_of_days * food_for_one_person

flag = False

for day in range(1, number_of_days + 1):
    
    chopping_wood_energy = float(input())

    group_energy -= chopping_wood_energy

    if group_energy <= 0:
        print(f"You will run out of energy. You will be left with {food_supply:.2f} food and {water_supply:.2f} water.")
        flag = True
        break

    if day % 2 == 0:
        group_energy += group_energy * 0.05
        water_supply -= water_supply * 0.3

    if day % 3 == 0:
        food_supply -= food_supply / number_of_players
        group_energy += group_energy * 0.1

if not flag:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")