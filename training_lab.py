from math import ceil, floor
l_m = float(input())
w_m = float(input())

l_cm = l_m * 100
w_cm = w_m * 100 - 100

w_mesta = floor(w_cm / 70)
l_mesta = floor(l_cm / 120)

total_mesta = w_mesta * l_mesta - 3

print(total_mesta)

