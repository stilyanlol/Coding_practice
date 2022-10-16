def add_subtract(a, b, c):

    def sum_numbers():
        return a + b

    def subtract():
        return sum_numbers() - c

    return subtract()


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_subtract(num1, num2, num3))