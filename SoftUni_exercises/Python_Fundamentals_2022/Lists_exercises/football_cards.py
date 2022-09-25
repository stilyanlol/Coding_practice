teams = input()

team_A_count = 11
team_B_count = 11

for item in ''.join(set(teams.split())):

    if team_A_count < 7 or team_B_count < 7:
        break

    if item == 'A':
        team_A_count -= 1
    elif item == 'B':
        team_B_count -= 1

print(f'Team A - {team_A_count}; Team B - {team_B_count}')

if team_A_count < 7 or team_B_count < 7:
    print('Game was terminated')
