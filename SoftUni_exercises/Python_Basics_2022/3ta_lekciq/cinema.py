type_of_projection = input()
numer_of_rows = int(input())
number_of_columns = int(input())

income = 0

capacity = numer_of_rows * number_of_columns

if type_of_projection == "Premiere":
    income = capacity * 12.00
elif type_of_projection == "Normal":
    income = capacity * 7.50
elif type_of_projection == "Discount":
    income = capacity * 5.00

print(f"{income:.2f} leva")
