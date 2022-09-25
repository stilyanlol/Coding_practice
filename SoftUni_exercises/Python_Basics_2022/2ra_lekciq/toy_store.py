puzzle = 2.6
talking_doll = 3
teddy_bear = 4.1
minion = 8.2
truck = 2

total_toys_sold = 0
winnings = 0
rent = 0

price_of_trip = float(input())
number_puzzles = int(input())
number_talking_dolls = int(input())
number_teddy_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

total = (number_trucks * truck) + (number_minions * minion) + (talking_doll * number_talking_dolls) + \
        (teddy_bear * number_teddy_bears) + (number_puzzles * puzzle)

total_toys_sold = number_trucks + number_minions + number_puzzles + number_teddy_bears + number_talking_dolls

if total_toys_sold >= 50:
    winnings = total - (0.25 * total)
else:
    winnings = total

rent = 0.1 * winnings
winnings -= rent

if price_of_trip <= winnings:
    print(f"Yes! {'%0.2f'%(winnings - price_of_trip)} lv left.")
else:
    print(f"Not enough money! {'%0.2f'%(price_of_trip - winnings)} lv needed.")