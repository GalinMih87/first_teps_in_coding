price_of_mackerel = float(input())
price_of_sprats = float(input())
price_of_mussels = 7.5
bonito_price = 0
price_of_saffron = 0

weight_of_bonito = float(input())
safrid_kg = float(input())
midi_kg = int(input())

bonito_price = price_of_mackerel + (price_of_mackerel * 0.6)
final_price_of_bonito = weight of bonito * bonito_price
price_of_saffron = price_of_sprats + (price_of_sprats * 0.8)
sum_safrid = safrid_kg * price_of_saffron
sum_midi = midi_kg * price_of_mussels

total = final_price_of_bonito + sum_safrid + sum_midi
print(f"{total:.2f}")
