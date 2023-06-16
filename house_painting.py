x = float(input())
y = float(input())
h = float(input())

#Wall
side_wall = x * y
window = 1.5 * 1.5
side = 2 * side_wall -2 * window
back_side = x * x
entrance = 1.2 * 2
front_and_back_wall = 2 * back_side - entrance

total_basics = side + front_and_back_wall
green_pain = total_basics / 3.4
print(f"{green_pain:.2f}")

#Roof

rectangle = 2 * (x * y)
triangle = 2 * (x * h / 2)
total_pokriv = rectangle + triangle
red_pain = total_pokriv / 4.3
print(f"{red_pain:.2f}")
