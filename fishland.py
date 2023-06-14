price_of_mackerel = float(input())
price_of_sprats = float(input())
price_of_mussels = 7.5
bonito_price = 0
price_of_safrid = 0

weight_of_bonito = float(input())
weight_of_safrid = float(input())
midi_kg = int(input())

bonito_price = price_of_mackerel + (price_of_mackerel * 0.6)
final_price_of_bonito = weight of bonito * bonito_price
price_of_safrid = price_of_sprats + (price_of_sprats * 0.8)
final_price_of_safrid = weight_of_safrid * price_of_safrid
sum_midi = midi_kg * price_of_mussels

total = final_price_of_bonito + final_price_of_safrid + sum_midi
print(f"{total:.2f}")
