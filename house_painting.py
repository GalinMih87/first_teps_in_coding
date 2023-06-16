x = float(input())
y = float(input())
h = float(input())

#steni
side_wall = x * y
window = 1.5 * 1.5
side = 2 * side_wall -2 * window
zadna_strana = x * x
vhod = 1.2 * 2
predna_zadna = 2 * zadna_strana - vhod

total_osnova = side + predna_zadna
green_pain = total_osnova / 3.4
print(f"{green_pain:.2f}")

#pokriv

pravoagalnik = 2 * (x * y)
triagalnik = 2 * (x * h / 2)
total_pokriv = pravoagalnik + triagalnik
red_pain = total_pokriv / 4.3
print(f"{red_pain:.2f}")
