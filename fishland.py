price_of_mackerel = float(input())
price_of_sprats = float(input())
price_of_mussels = 7.5
palamud_cena = 0
safrid_cena = 0

palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud_cena = price_of_mackerel + (price_of_mackerel * 0.6)
sum_palamud = palamud_kg * palamud_cena
safrid_cena = price_of_sprats + (price_of_sprats * 0.8)
sum_safrid = safrid_kg * safrid_cena
sum_midi = midi_kg * price_of_mussels

total = sum_palamud + sum_safrid + sum_midi
print(f"{total:.2f}")
