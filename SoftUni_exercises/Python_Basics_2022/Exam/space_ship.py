from math import floor

ship_width = float(input())
ship_lenght = float(input())
ship_height = float(input())
average_height_astronauts = float(input())

ship_cubics = ship_height * ship_lenght * ship_width
room_cubics = (average_height_astronauts + 0.4) * 2 * 2

needed_space = floor(ship_cubics / room_cubics)


if needed_space >= 3 and needed_space <= 10:
    print(f"The spacecraft holds {needed_space} astronauts.")

elif needed_space < 3:
    print("The spacecraft is too small.")

elif needed_space > 10:
    print("The spacecraft is too big.")

