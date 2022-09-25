hallCapacity = int(input())
peopleComingIn = input()

ticketPrice = 5
peopleInside = 0
totalIncome = 0


while peopleComingIn != "Movie time!":

    totalForEachIteration = 0

    peopleInside += int(peopleComingIn)
    totalForEachIteration += int(peopleComingIn) * ticketPrice

    if int(peopleComingIn) % 3 == 0:
        totalForEachIteration -= 5

    totalIncome += totalForEachIteration

    if peopleInside >= hallCapacity:

        if peopleInside == hallCapacity:
            print("There are 0 seats left in the cinema.")

            break

        hallCapacity = 0
        print("The cinema is full.")

        break

    peopleComingIn = input()

if peopleComingIn == "Movie time!":
    print(f"There are {hallCapacity - peopleInside} seats left in the cinema.")

print(f"Cinema income - {totalIncome} lv.")
