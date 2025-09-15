weight = int(input("Enter the weight of your luggage "))
length = int(input("Enter the length of your luggage "))
height = int(input("Enter the height of your luggage "))
width = int(input("Enter the width of your luggage "))

if weight > 8:
    print("Your luggage is to heavy")
elif length > 55:
    print("Your luggage is to long.")
elif height > 40:
    print("Your luggage is to tall.")
elif width > 23:
    print("Your luggage is to wide.")
else:
    print("You are allowed to bring your luggage")
              
