def continue_the_program():
    print("\nDo you wish to continue? \nPress (y) or (n): ")


tries_deposit = 0
tries_interest_rate = 0
tries_period_2 = 0
tries_period = 0
wrong_period = 3

print("Interest rate calculator \n\nIf you make three consecutive wrong period entries the"
      " program will automatically exit!")

start = input("\nStarting... \nPress Enter to continue.")

while True:

    if tries_deposit >= wrong_period or tries_interest_rate >= wrong_period or tries_period_2 >= wrong_period:
        print("You have exceeded the given number of times!")
        break

    deposit = input("\nEnter your initial deposit: ")

    if not deposit.isdigit():
        print("You have entered a string! \n\nPlease enter a integer.")
        tries_deposit += 1
        continue
    else:
        tries_deposit = 0

    deposit = int(deposit)

    if deposit >= 1:
        tries_deposit = 0

    if deposit < 1:
        print("\nDeposit can't be less than 1$!")

        tries_deposit += 1
        print("\nInvalid deposit!")

        if tries_deposit == 1 or tries_deposit == 2 or tries_deposit == 3:
            print(f"\nYou have {wrong_period - tries_deposit} left!")

    interest_rate = input("Enter your interest rate (percents): ")

    if not interest_rate.isdigit():
        print("You have entered a string! \n\nPlease enter a integer.")
        interest_rate += 1
        continue
    else:
        tries_deposit = 0

        interest_rate = int(interest_rate)

    if interest_rate >= 1:
        tries_interest_rate = 0

    if interest_rate < 1:
        print("\ninterest rate can't be less than 1%!")

        tries_interest_rate += 1
        print("\nInvalid interest rate!")

        if tries_interest_rate == 1 or tries_interest_rate == 2 or tries_interest_rate == 3:
            print(f"\nYou have {wrong_period - tries_interest_rate} left!")

    period = input("Enter the period up to 12 months: ")

    if not period.isdigit():
        print("You have entered a string! \n\nPlease enter a integer.")
        tries_period_2 += 1
        continue
    else:
        tries_deposit = 0

        period = int(period)

    if period >= 1:
        tries_period_2 = 0

    if period < 1:
        print("\nPeriod can't be less than 1%!")

        tries_period_2 += 1
        print("\nInvalid period!")

        if tries_period_2 == 1 or tries_period_2 == 2 or tries_period_2 == 3:
            print(f"\nYou have {wrong_period - tries_period_2} left!")

    if period <= 12:
        tries_period = 0

    if period > 12:
        tries_period += 1
        print("\nInvalid period!")

        if tries_period == 1 or tries_period == 2 or tries_period == 3:
            print(f"\nYou have {wrong_period - tries_period} left!")

        if tries_period >= wrong_period:
            print("\nYou exceeded the given number of tries!")
            break

        continue_the_program()
        choice = input()

        if choice == "n":
            print("\nThank you for using our program!")
            break

        else:
            continue

    total = ((period / 12) * deposit) * (interest_rate / 100)

    print(f"\nYour accumulated sum will be: {total:0.2f}$. \nYour total will be: {(total + deposit):0.2f}$.")

    continue_the_program()
    choice = input()

    if choice == "n":
        print("\nThank you for using our program!")
        break
