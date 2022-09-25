print("Half pyramid pattern of stars (*):")
for i in range(5):
    for j in range(i + 1):
        print("* ", end="")
    print()

print("Inverted half pyramid of stars (*):")
for i in range(5):
    for j in range(i, 5):
        print("* ", end="")
    print()

print("Full pyramid pattern of stars (*): ")
for i in range(5):
    for s in range(-6, -i):
        print(" ", end="")
    for j in range(i + 1):
        print("* ", end="")
    print()

# Print Star Pyramid of Given Size
print("Enter number of rows: ")
row = int(input())
print("Star pyramid of: " + str(row) + "Rows of lines:")
for i in range(row):
    for s in range(row, i, -1):
        print(end="")
    for j in range(i + 1):
        print(end="* ")
    print()
