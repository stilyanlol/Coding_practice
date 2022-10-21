number_of_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())

biggest_attendance = 0
total_bonus = (biggest_attendance / total_number_of_lectures) * (5 + additional_bonus)

for attendance in range(1, number_of_students + 1):
    attendance_each = int(input())
    if attendance_each > biggest_attendance:
        biggest_attendance = attendance_each

total_bonus = (biggest_attendance / total_number_of_lectures) * (5 + additional_bonus)
print(f'Max Bonus: {round(total_bonus)}.')
print(f'The student has attended {biggest_attendance} lectures.')