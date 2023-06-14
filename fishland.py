price_of_mackerel = float(input())
caca_cena = float(input())
midi_cena = 7.5
palamud_cena = 0
safrid_cena = 0

palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud_cena = price_of_mackerel + (price_of_mackerel * 0.6)
sum_palamud = palamud_kg * palamud_cena
safrid_cena = caca_cena + (caca_cena * 0.8)
sum_safrid = safrid_kg * safrid_cena
sum_midi = midi_kg * midi_cena

total = sum_palamud + sum_safrid + sum_midi
print(f"{total:.2f}")
