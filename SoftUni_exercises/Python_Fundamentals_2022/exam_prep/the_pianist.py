pieces_number = int(input())

pieces_dict = {}

for i in range(pieces_number):
    
    pieces = input().split('|')
    piece, composer, key = pieces[0], pieces[1], pieces[2]
    
    key_for_dict = piece
    value = {composer: key}
    pieces_dict[key_for_dict] = dict(value)   

command = input().split('|')

while command[0] != 'Stop':
    
    if command[0] == 'Add':
        
        piece, composer, key = command[1], command[2], command[3]
        
        if piece not in pieces_dict:
            key_for_dict = piece
            value = {composer: key}
            pieces_dict[key_for_dict] = dict(value)
            
            print(f"{piece} by {composer} in {key} added to the collection!")
            
        else:
            print(f'{piece} is already in the collection!')
            
    elif command[0] == 'Remove':
        
        piece = command[1]
        
        if piece in pieces_dict:
            del pieces_dict[piece]
            print(f"Successfully removed {piece}!")
            
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    
    elif command[0] == 'ChangeKey':
        
        piece, new_key = command[1], command[2]

        if piece in pieces_dict:
            pieces_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the.")
            
    command = input().split('|')
    
for key, value in pieces_dict.items():
    print(f"{key} -> {value.items()}")