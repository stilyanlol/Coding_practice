from math import pi

type_of_figure = input()

if type_of_figure == "square":
    side_a = float(input())
    side_a *= side_a
    print("%0.3f" %side_a)

if type_of_figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    s = side_a * side_b
    print("%0.3f" %s)

if type_of_figure == "circle":
    r = float(input())
    s = pi * r**2
    print("%0.3f" %s)

if type_of_figure == "triangle":
    side_a = float(input())
    height = float(input())
    s = (side_a * height) / 2
    print("%0.3f" %s)