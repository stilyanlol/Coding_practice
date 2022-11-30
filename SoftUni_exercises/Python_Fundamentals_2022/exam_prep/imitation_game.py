message = [x for x in input()]

command = input().split('|')

while command[0] != 'Decode':
    
    if command[0] == 'Move':
        num_of_letters = int(command[1])
        for i in range(num_of_letters):
            current_letter = message[0]
            del message[0]
            message.append(current_letter)
            
    if command[0] == 'Insert':
        index = int(command[1])
        value = command[2]
        message.insert(index, value)
    
    if command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        str_message = ''.join(message)
        str_message = str_message.replace(substring, replacement)
        message = [x for x in str_message]
    
    command = input().split('|')

decrypted_message = ''.join(message)
print(f"The decrypted message is: {decrypted_message}")
