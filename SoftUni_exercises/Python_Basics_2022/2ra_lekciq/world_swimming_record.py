import math

current_record = float(input())
record_meters = float(input())
time_for_one_meter = float(input())

needed_swimming_time = record_meters * time_for_one_meter

water_resistance = math.floor(record_meters / 15) * 12.5

total_time = needed_swimming_time + water_resistance

if total_time < current_record:
    print(f"Yes, he succeeded! The new world record is {'%0.2f' % total_time} seconds.")
else:
    print(f"No, he failed! He was {'%0.2f' % (total_time - current_record)} seconds slower.")
