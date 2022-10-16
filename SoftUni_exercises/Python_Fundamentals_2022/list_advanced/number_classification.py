numnbers = [int(num) for num in input().split(', ')]

positive = [num for num in numnbers if num >= 0]
negative = [num for num in numnbers if num < 0]
even = [num for num in numnbers if num % 2 == 0]
odd = [num for num in numnbers if num % 2 != 0]

print(f"Positive: {', '.join(map(str, positive))}")
print(f"Negative: {', '.join(map(str, negative))}")
print(f"Even: {', '.join(map(str, even))}")
print(f"Odd: {', '.join(map(str, odd))}")