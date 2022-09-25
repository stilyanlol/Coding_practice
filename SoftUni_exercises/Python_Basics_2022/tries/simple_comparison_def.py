# Creating a comparison program.
a = int(input("Enter a:"))
b = int(input("Enter b:"))

if a < b:
    print("a e po - malko ot b")

elif a == b:
    print("a e ravno na b")

elif a > b:
    print("a e po - golqmo ot b")


# Creating a function that does the same thing but we can call it as many times as we need.
def comparison_baby():
    c = int(input("Enter c:"))
    d = int(input("Enter d:"))

    if c < d:
        print("c e po - malko ot d")

    elif c == d:
        print("c e ravno na d")

    elif c > d:
        print("c e po - golqmo ot d")


# Calling the function.
comparison_baby()
