number_of_plants = int(input())

all_plants = {}
plants_rating = {}

for plants in range(number_of_plants):
    plant, rarity = input().split("<->")
    key = plant
    value = int(rarity)
    all_plants[key] = value
    
action = input().split(": ")

while action[0] != "Exhibition":
    
    if action[0] == "Rate":
        plant, rating = action[1].split(" - ")
        plants_rating[plant] = [int(rating)]
        
        if plant in all_plants.keys():
            plants_rating[plant].append(int(rating))
        else: continue
        
    elif action[0] == "Update":
        plant, new_rarity = action[1].split(" - ")
        
        if plant in all_plants.keys():
            all_plants[plant] = int(new_rarity)
        else: continue

    elif action[0] == "Reset":
        plant = action[1]
        
        if plant in all_plants.keys():
            del plants_rating[plant]
            plants_rating[plant] = 0
        else: continue
        
    action = input().split(": ")

print(all_plants.keys(), all_plants.values())
print(plants_rating.keys(), plants_rating.values())
