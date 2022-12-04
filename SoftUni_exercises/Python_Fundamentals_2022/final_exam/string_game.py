initial_string = input()

command = input().split()

while command[0] != "Done":
    
    if command[0] == "Change":
        
        char, replacement = command[1], command[2]
        
        if char in initial_string:
            initial_string = initial_string.replace(char, replacement)
            print(initial_string)
        else:
            print(initial_string)
    
    elif command[0] == "Includes":
        
        substring = command[1]
        
        if substring in initial_string:
            print(True)
        else:
            print(False)
    
    elif command[0] == "End":
        
        end_substring = command[1]
        
        if initial_string.endswith(end_substring):
            print(True)
        else:
            print(False)
    
    elif command[0] == "Uppercase":
        
        initial_string = initial_string.upper()
        print(initial_string)
    
    elif command[0] == "FindIndex":
        
        character = command[1]
        
        for ch in initial_string:
            if character in initial_string:
                print(initial_string.index(character))
                break
    
    elif command[0] == "Cut":
        
        start_index, count = int(command[1]), int(command[2])
        
        if len(initial_string) > start_index + count:
            initial_string_copy = initial_string
            initial_string_copy = initial_string_copy[0: start_index + 1:] + initial_string_copy[start_index + count::]
            print(initial_string[start_index:(start_index + count)])
              
    command = input().split()