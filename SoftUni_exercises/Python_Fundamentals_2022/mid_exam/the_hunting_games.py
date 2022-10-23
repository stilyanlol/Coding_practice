number_of_days = int(input())
number_of_players = int(input())
group_energy = float(input())
water_for_one_person = float(input())
food_for_one_person = float(input())

water_supply = number_of_players * water_for_one_person
food_supply = number_of_players * food_for_one_person


for day in range(1, number_of_days + 1):
    
    chopping_wood_energy = float(input())

    group_energy -= chopping_wood_energy

    if day % 2 == 0:
        group_energy += group_energy * 0.05
        water_supply -= water_for_one_person * 0.3

    if day % 3 == 0:
        food_supply -= food_supply / number_of_players
        group_energy += group_energy * 0.1

    if group_energy <= 0:
        print(f"You will run out of energy. You will be left with {food_supply} food and {water_supply} water.")
        break

print(f"You are ready for the quest. You will be left with - {group_energy} energy!")