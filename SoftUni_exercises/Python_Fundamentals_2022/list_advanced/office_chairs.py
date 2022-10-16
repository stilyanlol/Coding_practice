# number_of_rooms = int(input())

# free_chairs = 0

# for number_of_room in range(1, number_of_rooms + 1):

#     available_chairs, visitors_now = input().split()
#     num_of_chairs = len(available_chairs)
#     visitors = int(visitors_now)

#     if num_of_chairs < visitors:
#         needed_chairs_in_room = visitors - num_of_chairs
#         print(f'{needed_chairs_in_room} more chairs needed in room {number_of_room}')
    
#     elif num_of_chairs > visitors:
#             free_chairs += num_of_chairs - visitors

# if free_chairs > visitors:
#     print(f'Game On, {free_chairs} free chairs left')

def check_the_rooms(numbers_of_rooms):
    total_free_chairs = 0
    total_needed_chairs = 0
    for room in range(1, numbers_of_rooms + 1):
        free_chairs, visitors = input().split()
        difference = len(free_chairs) - int(visitors)
        if difference >= 0:
            total_free_chairs += difference
        else:
            total_needed_chairs += abs(difference)
            print(f"{abs(difference)} more chairs needed in room {room}")
    return total_free_chairs, total_needed_chairs
 
 
number_of_rooms = int(input())
free_chairs, needed_chairs = check_the_rooms(number_of_rooms)
if free_chairs >= needed_chairs:
    print(f"Game On, {free_chairs} free chairs left")