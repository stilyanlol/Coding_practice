def calculate(operation, num1, num2):
    if operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2
    elif operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2


operation = input()
num1 = int(input())
num2 = int(input())

result = calculate(operation, num1, num2)

print(int(result))