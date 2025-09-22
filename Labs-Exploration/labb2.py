import numpy as np
import matplotlib.pyplot as plt

path1 = "//Users/wilgotlucaci/Desktop/Labb2/testpoints.txt" # Sätter en path för testpoints.txt filen
path2 = "/Users/wilgotlucaci/Desktop/Labb2/datapoints.txt" #Sätter en path för datapoints.txt filen


testpoints = [] #Skapar en tom lista

with open(path1, "r")as t: # Öppnar path 1 
    testpoints_lines = t.read().splitlines() #Sätter tespoints.txt med variabel namn testpoints_lines + att jag ger den läsrättighter + tar bort att det blir ny rad för varje punkt

for line in testpoints_lines[1:]: # Jag hoppar över titlen på filen
    if not line:
        continue

    line = line.replace("(", "").replace(")","") # Jag tar bort alla ( och ) och byter ut dom mot inget

    parts = line.split() # Delar upp de olika "parts"
    x = parts[1].replace(",", "") # Byter ut , mot "inget" + ger x ett värde för varje punkt på listan
    y = parts[2] # Ger y ett värde för varje punkt på listan

    testpoints.append((float(x), float(y)))# Fyller den tomma listan jag skapade på ln 8 med x,y kordinater

coordinates = [] #Skapar tom lista
type_figure = [] #Skapar tim lista


with open(path2, "r") as d: #Öppnar path2
    datapoints_lines = d.read().splitlines() 

for line in datapoints_lines[1:]:
    if not line:
        continue

    delar = [d.strip() for d in line.split(",")]
    x1, y1, z1 = (float(delar[0])), (float(delar[1])), (int(delar[2]))
    coordinates.append((x1,y1))
    type_figure.append(z1)

xs, ys = zip(*coordinates)


plt.figure(dpi= 200)
plt.scatter(xs,ys)
plt.title("Width x Length")
plt.xlabel("Width")
plt.ylabel("Height")
plt.show()

