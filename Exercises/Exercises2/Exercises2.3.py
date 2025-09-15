import random as rnd
guesses = 0
number1 = rnd.randint(1,100)

while True:
    guess = int(input("Guess a number between 1 and 100. "))
    guesses += 1
    if guess == number1:
        print(f"Correct, You won in {guesses} guesses.") 
        break
    elif guess > number1:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")