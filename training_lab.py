from math import ceil, floor
l_m = float(input())
w_m = float(input())

l_cm = l_m * 100
w_cm = w_m * 100 - 100

w_seat = floor(w_cm / 70)
l_seat = floor(l_cm / 120)

total_seat = w_seat * l_seat - 3

print(total_seat)

