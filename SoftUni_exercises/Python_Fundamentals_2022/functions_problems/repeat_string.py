# def repeater(string, counter):
#     return string * counter


# new_string = input()
# counter = int(input())
# print(repeater(new_string, counter))

new_string = input()
counter = int(input())
result = lambda string, counter: new_string * counter
print(result(new_string, counter))