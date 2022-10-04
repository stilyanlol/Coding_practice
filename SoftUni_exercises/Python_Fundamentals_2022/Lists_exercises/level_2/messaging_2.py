numbers = input().split()
message = input()

new_message_list = []
index_list = []
final_message = []

#separate all the characters into a list for clearer look
for ch in message:
    new_message_list.append(ch)
#<-----------------------------------------

#from here ---------------------------->
for num in numbers:
    num_index = []
    
    for i in num:
        num_index.append(int(i))
        given_index = (sum(num_index))
#<---- to here we find the index number, 
#aka the sum of each number in the list

#-------->script for finding and removing the
#tring and value
    for ch in range(0, len(new_message_list) + given_index):
        if ch == given_index:
            final_message.append(new_message_list[ch])
            new_message_list.remove([ch])
#<-------------------------------------------

print(''.join(final_message))