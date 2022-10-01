cards = input()
shuffle_count = int(input())

list_cards = cards.split()

odd_list = []
even_list = []

shuffled_list = even_list + odd_list

for i in range(0, len(list_cards)):
	if i % 2 == 0:
		even_list.append(list_cards[i])
	if i % 2 != 0:
		odd_list.append(list_cards[i])

for shuffle in range(shuffle_count):
	for j in range(0, len(shuffled_list)):
		if j % 2 == 0:
			even_list.append(shuffled_list[j])
		if j % 2 != 0:
			odd_list.append(shuffled_list[j])

shuffled_list = even_list + odd_list

print(shuffled_list)