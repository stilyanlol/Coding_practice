import math

name_of_tv_show = input()
episode_time = float(input())
total_rest_time = float(input())

lunch_time = total_rest_time / 8
small_rest_time = total_rest_time / 4

if total_rest_time >= episode_time + lunch_time + small_rest_time:
    print(f"You have enough time to watch {name_of_tv_show} and left with"
          f" {math.ceil(total_rest_time - (episode_time + lunch_time + small_rest_time))} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_tv_show}, you need"
          f" {math.ceil((episode_time + lunch_time + small_rest_time) - total_rest_time)} more minutes.")
