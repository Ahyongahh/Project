import math

def round_to_2_sig(number):
    if number == 0:
        return 0
    else:
        order_of_magnitiude = math.floor(math.log10(abs(number)))
        scale = 10 ** (2 - order_of_magnitiude - 1)
        return round(number * scale) / scale
    

height_in_metres = float(input('Whats your height in m?: '))
weight_in_kg = int(input("What's your weight in kg?: "))

ft = height_in_metres * 3.281
pound = weight_in_kg * 2.205
rounded_height = round_to_2_sig(ft)


print("your height in ft is", rounded_height, "and your weight in lbs is", pound)
