import numpy as np
import matplotlib.pyplot as plt
import os

path = "/Users/wilgotlucaci/python-programming-WILGOT-LUCACI/Labs-Exploration"

data = np.genfromtxt(
    "/Users/wilgotlucaci/Desktop/Labb3/unlabelled_data.csv", 
    delimiter = ","
)

x = data[:, 0].astype(float)
y = data[:, 1].astype(float)

#x1, y1 = x[0], y[0]
#x2, y2 = x[-1], y[-1]

#k = (y2 - y1) / (x2 - x1)
#m = y1 - k * x1
k, m = np.polyfit(x, y, 1)

line_x = np.linspace(min(x), max(x), 100)
line_y = k * line_x + m

def classify(x_point, y_point):
    y_line = k * x_point + m
    if y_point > y_line:
        return "1"
    elif y_point < y_line:
        return "0"
    else:
        return "På linjen"
    
classifications = [classify (x[i], y[i]) for i in range(len(x))]


#above = 0
#under = 0
#for c in classifications:
    #if c == "1":
        #above += 1
    #elif c == "0":
        #under += 1

labelleddata = os.path.join(path, "labelled_data.csv")
with open(labelleddata, "w") as s:
    for i in range (len(x)):
        s.write(f"({x[i]}, {y[i]}) --> {classifications[i]}\n")




plt.figure(figsize=(8,5))
plt.plot(line_x, line_y, linewidth= 4, color= "g")
plt.scatter(x,y)
plt.title("Linear classification")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True, color= "c")
plt.show() 



