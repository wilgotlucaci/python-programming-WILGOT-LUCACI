#Uppgift 6
import math
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