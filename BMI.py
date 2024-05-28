import math

def round_to_2_sig(number):
    if number == 0:
        return 0
    else:
        order_of_magnitiude = math.floor(math.log10(abs(number)))
        scale = 10 ** (2 - order_of_magnitiude - 1)
        return round(number * scale) / scale
    
Height = int(input("What's your Height in CM?"))
Weight = int(input("What's your weight in kg?"))

Value1 = Height * Height/10000
Answer = Weight/Value1

rounded_answer = round_to_2_sig(Answer)

if rounded_answer < 18.5:
    print("Your BMI of" , rounded_answer , "Puts you Underweight")
elif 18.5 <= rounded_answer <= 22.9:
     print("Your BMI of" , rounded_answer , "Puts you Normal")
elif 23 <= rounded_answer <= 29.9:
    print("Your BMI of" , rounded_answer , "Puts you Overweight")
else:
    print("Your BMI of" , rounded_answer , "Puts you Obese")


