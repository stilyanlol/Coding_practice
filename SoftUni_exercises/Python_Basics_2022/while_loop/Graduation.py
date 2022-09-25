name_of_student = input()

year = 0
average_grade = 0
sum_count = 0
failed_years = 0

while True:

    annual_grade = float(input())
    year += 1

    if annual_grade < 4:

        failed_years += 1

        if failed_years == 2:
            print(f"{name_of_student} has been excluded at {year} grade")
            break

        year -= 1

    else:
        sum_count += annual_grade



    if year == 12:

        average_grade = sum_count / 12

        print(f"{name_of_student} graduated. Average grade: {average_grade:0.2f}")
        break