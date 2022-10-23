travel_route = input().split('||')
starting_amount_fuel = int(input())
starting_amount_ammo = int(input())

current_fuel = starting_amount_fuel
current_ammo = starting_amount_ammo
flag = False

while True:

    if flag:
        break

    for element in travel_route:

        if 'Titan' in element:
            print('You have reached Titan, all passengers are safe.')
            flag = True
            break

        elif 'Travel' in element:

            command, number = element.split(' ')

            if int(number) < current_fuel:
                current_fuel -= int(number)
                print(f'The spaceship travelled {number} light-years.')
            else:
                print('Mission failed.')
                flag = True
                break

        elif 'Enemy' in element:

            command, number = element.split(' ')

            if current_ammo >= int(number):
                current_ammo -= int(number)
                print(f'An enemy with {number} armour is defeated.')
            elif current_ammo < int(number):
                current_fuel -= int(number) * 2
                print(f'An enemy with {number} armour is outmaneuvered.')
            else:
                print('Mission failed.')
                break

        elif 'Repair' in element:

            command, number = element.split(' ')

            current_fuel += int(number)
            current_ammo += int(number) * 2
            print(f'Ammunitions added: {int(number) * 2}.')
            print(f'Fuel added: {int(number)}.')