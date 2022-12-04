friends = {}

command = input().split(": ")

while command[0] != "Log out":
    
    if command[0] == "New follower":
        username = command[1]
        
        if username not in friends.keys():
            friends[username] = [0, 0]
        
    elif command[0] == "Like":
        username, count = command[1], int(command[2])
        
        if username not in friends.keys():
            friends[username] = [count, 0]
        else:
            friends[username][0] += count
    
    elif command[0] == "Comment":
        username = command[1]
        
        if username not in friends.keys():
            friends[username] = [0, 1]
        else:
            friends[username][1] += 1
    
    elif command[0] == "Blocked":
        username = command[1]
        
        if username in friends.keys():
            del friends[username]
        else:
            print(f"{username} doesn't exist.")
    
    command = input().split(": ")
  
print(f"{len(friends)} followers")

for name, stats in friends.items():
    print(f"{name}: {sum(stats)}")
