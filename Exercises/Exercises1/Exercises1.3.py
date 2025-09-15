#Exercise 3

a = int(input("Enter the first angle. "))
b = int(input("Enter the second angle. "))
c = int(input("Enter the third angle. "))

if a > 0 and b > 0 and c > 0:
    if a + b + c == 180:
        print("You have a valid triangle.")
        if a == 90 or b == 90 or c == 90:
            print("Your triangle has a right angle.")
        else:
            print("Your triangle does not have a right angle.")
    else:
        print("The angles do not add up to 180, therefore it is not a triangle.")
else:
    print("All angles must be positive.")