def main_func(initial_sequence):
    
    counter = 0
    
    while True:

        command = input().split()
        
        if command[0] == 'end':
            stringed = [str(x) for x in initial_sequence]
            print('Sorry you lose :(')
            print(' '.join(stringed))
            break
        
        index_1 = int(command[0])
        index_2 = int(command[1])
        
        counter += 1
        
        if index_1 == index_2 or index_1 < 0 or index_1 > len(initial_sequence) or index_2 < 0 or index_1 > len(initial_sequence):
            middle_of_seq = len(intital_sequence)//2 
            initial_sequence.insert(middle_of_seq, f'-{counter}a')
            initial_sequence.insert(middle_of_seq, f'-{counter}a')
            print("Invalid input! Adding additional elements to the board")
        
        elif initial_sequence[index_1] == intital_sequence[index_2]:
            initial_sequence.pop(index_1)
            initial_sequence.pop(index_2)
            print(f"Congrats! You have found matching elements - {initial_sequence[index_1]}!")
            
        elif initial_sequence[index_1] != intital_sequence[index_2]:
            print("Try again!")
            
        elif len(initial_sequence) <= 0:
            print(f"You have won in {counter} turns!")


intital_sequence = input().split()
main_func(intital_sequence)