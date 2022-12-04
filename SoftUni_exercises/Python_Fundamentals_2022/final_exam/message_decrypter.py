import re

num_of_tries = int(input())

pattern = r"^([$\%])([A-Z][a-z]{3,})\1:\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"

for _ in range(num_of_tries):
    
    message = input()
    
    result = re.search(pattern, message)
    
    if result:
        
        tag, ch_1, ch_2, ch_3 = result.groups(1)[1], result.groups(2)[2], result.groups(3)[3], result.groups(4)[4]
        
        print(f"{tag}: {chr(int(ch_1))}{chr(int(ch_2))}{chr(int(ch_3))}")
        
    else:
        print("Valid message not found!")