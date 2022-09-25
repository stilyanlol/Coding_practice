price_of_strawberries = float(input())
kilograms_bananas = float(input())
kilograms_oranges = float(input())
kilograms_berries = float(input())
kilograms_strawberries = float(input())

price_of_berries = price_of_strawberries / 2
price_of_oranges = price_of_berries * 0.6
price_of_bananas = price_of_berries * 0.2

total = (price_of_bananas * kilograms_bananas) + (price_of_oranges * kilograms_oranges)\
        + (price_of_berries * kilograms_berries)\
        + (price_of_strawberries * kilograms_strawberries)

print(f"{total:0.2f}")
