initial_string = input()

start_index = 5
count = 5
        
if len(initial_string) > start_index + count:
    initial_string_copy = initial_string
    initial_string_copy = initial_string_copy[0: start_index + 1:] + initial_string_copy[start_index + count::]
    print(initial_string[start_index + 1:(start_index + count)])
    