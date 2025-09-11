#Uppgift 1

import math
a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(c)

a = 5
c = 7
b = math.sqrt(c**2 - a**2)

print(b)

#Uppgift 2

predictions = 356
correct_predictions = 300

accuracy = correct_predictions / predictions
print(accuracy)

#Uppgift 3

TP = 2
FP = 2
FN = 11
TN = 985

accuracy = (TP + TN) / (TP + TN + FP + FN)
print(accuracy)


#Uppgift 4

x1 = 4
x2 = 0
y1 = 4
y2 = 1

k=(y2 - y1) / (x2 - x1) 
y = k + y1
m = y1 - k*x1
print(k)
print(m)


#Uppgift 5

x1 = 3
y1 = 5
x2 = -2
y2 = 4

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(distance)

#Uppgift 6

p1 = 2
p2 = 1
p3 = 4
q1 = 3
q2 = 1
q3 = 0

p = (p1, p2, p3)
q = (q1, q2, q3)

distance = math.sqrt((q1 - p1)**2 + (q2 - p2)**2 + (q3 - p3)**2)
print(distance)

print(helloworld)