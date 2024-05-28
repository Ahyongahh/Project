import random

Value = random.randint(0,100)
low,high = 0,100

while True:

    guess = int(input(f"Guess the number between {low} and {high}: "))

    if guess == Value:
        print("Correct the number was", Value)
        break

    elif guess < Value:
        print("Incorrect, try again. The Number is higher than", guess)
        low = guess +1 #update the lower bound

    elif guess > Value:
        print("Incorrect, Try again. The Number is lower than", guess)
        high = guess -1 #Update the higher bound

