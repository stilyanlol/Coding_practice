import re, math


line = input()

pattern = r'([|#])(?P<item_name>[A-Za-z ]+)\1(?P<date>\d{2}\/\d{2}\/\d{2})\1(?P<calories>\d{1,5})\1'

result = re.findall(pattern, line)

food = []
date_s = []
sum_lis = []
    
for match in re.finditer(pattern, line):
    item_name = match['item_name']
    food.append(item_name)
    
    date = match['date']
    date_s.append(date)
    
    calorie_cnt = match["calories"]
    sum_lis.append(int(calorie_cnt))

total_days = (math.floor(sum(sum_lis) / 2000))
print(f'You have food to last you for: {total_days} days!')

for i in range(len(food)):
    print(f'Item: {food[i]}, Best before: {date_s[i]}, Nutrition: {int(sum_lis[i])}')

