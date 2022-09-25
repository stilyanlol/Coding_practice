import math

number_of_paint_boxes = int(input())
number_of_wallpaper_rolls = int(input())
price_of_one_pair_of_gloves = float(input())
price_of_one_brush = float(input())

price_of_one_box_of_paint = 21.50
price_of_one_wallpaper_roll = 5.20

total_paint = number_of_paint_boxes * price_of_one_box_of_paint
total_wallpapers = number_of_wallpaper_rolls * price_of_one_wallpaper_roll

number_of_gloves_needed = math.ceil(number_of_wallpaper_rolls * 0.35)
number_of_paint_brushes_needed = math.floor(number_of_paint_boxes * 0.48)

total_gloves = number_of_gloves_needed * price_of_one_pair_of_gloves
total_brushes = number_of_paint_brushes_needed * price_of_one_brush

total_delivery_cost = (total_paint + total_wallpapers + total_gloves + total_brushes) / 15

print(f"This delivery will cost {total_delivery_cost:0.2f} lv.")
