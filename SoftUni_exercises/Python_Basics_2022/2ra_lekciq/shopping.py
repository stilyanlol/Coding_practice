budget = float(input())
number_of_GPUs = int(input())
number_of_CPUs = int(input())
number_of_RAM = int(input())

GPU_price = 250
CPU_price = 0.35 * (number_of_GPUs * GPU_price)
RAM_price = 0.1 * (number_of_GPUs * GPU_price)

total = (number_of_GPUs * GPU_price) + (number_of_CPUs * CPU_price) + (number_of_RAM * RAM_price)

if number_of_GPUs > number_of_CPUs:
    total = total - (0.15 * total)

if budget >= total:
    print(f"You have {'%0.2f' % (budget - total)} leva left!")
else:
    print(f"Not enough money! You need {'%0.2f' % (total - budget)} leva more!")
