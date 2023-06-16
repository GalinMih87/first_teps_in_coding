vegetables = float(input())
fruits = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())
euro = 1.94

vegetables_sum = vegetables * vegetables_kg
fruits_sum = fruits * fruits_kg

total = (vegetables_sum + fruits_sum) / euro

print(f"{total:.2f}")
