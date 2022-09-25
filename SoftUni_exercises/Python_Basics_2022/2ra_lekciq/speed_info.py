speed = float(input())

if speed <= 10:
    print("slow")
elif speed > 9 and speed <= 50:
    print("average")
elif speed > 49 and speed <= 150:
    print("fast")
elif speed > 149 and speed <= 1000:
    print("ultra fast")
else:
    print("extremely fast")