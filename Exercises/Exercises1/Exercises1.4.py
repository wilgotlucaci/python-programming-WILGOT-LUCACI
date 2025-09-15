#Execercise 4

weight = int(input("Enter your weight. "))
age = int(input("Enter your age. "))

if age > 12 and weight > 40:
    print("You can take 1-2 pills.")
elif 7 <= age <= 12 and 25 <= weight <= 40:
    print("You can take 1/2 - 1 pill.")
elif 3 <= age <= 7 and 15 <= weight <= 25:
    print("You should take half a pill")  