num = int(input("Enter a number. "))
if num % 2 == 0:  
    print("The number is even.")
else:
    print("The number is odd")
if num % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")
if num % 5 == 0 and num % 2 == 1:
    print("The number is divisible by 5 and odd.")
elif num % 5 == 0 and num % 2 == 0:
    print("The number is divisible by 5 and even.")
else:
    print("The number is not divisible by 5.")