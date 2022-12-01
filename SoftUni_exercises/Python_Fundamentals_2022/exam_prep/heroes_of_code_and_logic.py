num_of_players = int(input())

heroes = {}

for i in range(num_of_players):
    heroes_stats = input().split()
    key_name_of_hero = heroes_stats[0]
    value_hp = int(heroes_stats[1])
    value_mp = int(heroes_stats[2])
    heroes[key_name_of_hero] = [value_hp]
    heroes[key_name_of_hero].append(value_mp)

command = input().split(" - ")

while command[0] != "End":
    
    if command[0] == "CastSpell":
        hero_name, mp_needed, spell_name = command[1], int(command[2]), command[3]
        
        if heroes[hero_name][1] >= mp_needed:
            heroes[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    
    elif command[0] == "TakeDamage":
        hero_name, damage, attacker = command[1], int(command[2]), command[3]
        
        if heroes[hero_name][0] > damage:
            heroes[hero_name][0] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
    
    elif command[0] == "Recharge":
        hero_name, amount = command[1], int(command[2])
        
        heroes[hero_name][1] += amount
        
        if heroes[hero_name][1] > 200:
            real_amount = amount - (heroes[hero_name][1] - 200)
            print(f"{hero_name} recharged for {real_amount} MP!")
            heroes[hero_name][1] = 200

        else:
            print(f"{hero_name} recharged for {amount} MP!")
    
    elif command[0] == "Heal":
        hero_name, amount = command[1], int(command[2])
        
        heroes[hero_name][0] += amount
        
        if heroes[hero_name][0] > 100:
            real_amount = amount - (heroes[hero_name][0] - 100)
            print(f"{hero_name} healed for {real_amount} HP!")
            heroes[hero_name][0] = 100

        else:
            print(f"{hero_name} healed for {amount} HP!")
    
    command = input().split(" - ")
    
for name, stats in heroes.items():
    print(name)
    print(f"  HP: {stats[0]}")
    print(f"  MP: {stats[1]}")