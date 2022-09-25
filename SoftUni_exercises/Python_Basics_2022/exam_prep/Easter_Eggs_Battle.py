eggs_first_competitor = int(input())
eggs_second_competitor = int(input())

while True:

    command = input()

    if command == "End":
        print(f"Player one has {eggs_first_competitor} eggs left.")
        print(f"Player two has {eggs_second_competitor} eggs left.")
        break

    elif command == "one":
        eggs_second_competitor -= 1

        if eggs_second_competitor == 0:
            print(f"Player two is out of eggs. " 
                  f"Player one has {eggs_first_competitor} eggs left.")
            break

    elif command == "two":
        eggs_first_competitor -= 1

        if eggs_first_competitor == 0:
            print(f"Player one is out of eggs. "
                  f"Player two has {eggs_second_competitor} eggs left.")
            break
