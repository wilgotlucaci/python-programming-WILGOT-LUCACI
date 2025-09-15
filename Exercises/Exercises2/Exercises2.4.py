import random as rnd

score = 1

while True:
    print("Hello Welcome to the game")
    print("Choose game mode:")
    print("1. Easy (numbers 1-5)")
    print("2. Medium (numbers 1-10)")
    print("3. Hard (numbers 1-20)")
    gamemode = int(input("Choose 1,2,3: "))
    while gamemode == 1:
        num1 = rnd.randint(1,5)
        num2 = rnd.randint(1,5)
        answer = int(input(f"What is {num1} times {num2}? "))
        if answer == num1 * num2:
            print("Correct, 1 point")
            print(f"Your score is {score}.")
            score += 1
        if score > 10:
                print("You won the game, Good job")
                break
        else:
            print("Not correct sorry.")
    
    while gamemode == 2:
        num1 = rnd.randint(1,10)
        num2 = rnd.randint(1,10)
        answer = int(input(f"What is {num1} times {num2}? "))
        if answer == num1 * num2:
            print("Correct, 1 point")
            print(f"Your score is {score}.")
            score += 1
        if score > 10:
            print("You won the game, Good job")
            break
        else:
            print("Not correct sorry.")

    while gamemode == 3:
        num1 = rnd.randint(1,20)
        num2 = rnd.randint(1,20)
        answer = int(input(f"What is {num1} times {num2}? "))
        if answer == num1 * num2:
            print("Correct, 1 point")
            print(f"Your score is {score}.")
            score += 1
        if score > 10:
            print("You won the game, Good job")
            break
        else:
            print("Not correct sorry.")
