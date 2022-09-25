n = int(input())
salary = int(input())


for i in range(1, n + 1):

    name_of_tab = input()

    if name_of_tab == "Facebook":
        salary -= 150
    elif name_of_tab == "Instagram":
        salary -= 100
    elif name_of_tab == "Reddit":
        salary -= 50

    if salary <= 0:
        print(f"You have lost your salary.")
        break

if salary > 0:
    print(salary)
