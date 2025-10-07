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

def classify(x_point, y_point, k, m):
    y_line = k * x_point + m
    if y_point > y_line:
        return "1"
    elif y_point < y_line:
        return "0"
    else:
        return "På linjen"
    
classifications = [classify(xi, yi, k, m ) for xi, yi in zip(x,y)]
f_classification = [classify(xi, yi, -0.489, 0) for xi, yi in zip(x,y)]
g_classification = [classify(xi,yi, -2, 0.16) for xi, yi in zip(x, y)]
h_classification = [classify(xi, yi, 800, -120) for xi, yi in zip(x, y)]

labelleddata = os.path.join(path, "labelled_data.csv")
with open(labelleddata, "w") as s:
    for i in range (len(x)):
        s.write(f"({x[i]}, {y[i]}) --> {classifications[i]}\n")
print("Writing labelled data to labelled_data.csv file")


f_x = -0.489 * line_x
g_x = -2 * line_x + 0.16
h_x = 800 * line_x -120


plt.figure(figsize=(8,5))
plt.plot(line_x, line_y, linewidth= 3, label= "Data", color= "r")
plt.scatter(x,y)
plt.plot(line_x, f_x, label= "f(x) = -0.489x",linewidth= 3,color= "b")
plt.plot(line_x, g_x, label= "g(x) = -2x + 0.16",linewidth= 3,color= "m")
plt.plot(line_x, h_x, label= "h(x) = 800x -120", linewidth= 3,color= "g")
plt.ylim(-10,10)
plt.title("Linear classification")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True, color= "c")
plt.show() 



