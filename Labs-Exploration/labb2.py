# Vill tlägga att jag tagit hjlp av både copliot och chat-gpt när jag kort fast eller fått ett error som jag inte fattat

import matplotlib.pyplot as plt
import math

path1 = "//Users/wilgotlucaci/Desktop/Labb2/testpoints.txt" 
path2 = "/Users/wilgotlucaci/Desktop/Labb2/datapoints.txt" 

testpoints = [] 

with open(path1, "r")as t: 
    testpoints_lines = t.read().splitlines() 
    #Sätter tespoints.txt med variabel namn testpoints_lines + att jag ger den läsrättighter + tar bort att det blir ny rad för varje punkt

for line in testpoints_lines[1:]: # hoppar över titlen på filen
    if not line:
        continue

    # Tar bort paranteser, tar bort komman.    
    line = line.replace("(", "").replace(")","") 
    parts = line.split()
    x = parts[1].replace(",", "") 
    y = parts[2] 

    #Fyller  "Tespoints med x och y värden."
    testpoints.append((float(x), float(y)))

coordinates = [] 
type_figure = []


with open(path2, "r") as d: 
    datapoints_lines = d.read().splitlines() 
    # Ger datapoints.txt varibelnamnet datapoints_lines och ger läsrättighter

for line in datapoints_lines[1:]: #Hoppar över första raden
    if not line:
        continue

    # Skapar en lista med ny rad för varje koordinat + tar bort mellanslag    
    delar = [d.strip() for d in line.split(",")] 
    x1, y1, z1 = (float(delar[0])), (float(delar[1])), (int(delar[2]))
    coordinates.append((x1,y1))
    type_figure.append(z1)

xs, ys = zip(*coordinates)

test_x1, test_y1 = [], []
test_x2, test_y2 = [], []


nn = 10 #Nearest neighbor = 10

for tp in testpoints:
    distances = []
    
    # Beräknar euklidiskt avstånd mellan tespunkt tp och träningspunkterna coord
    
    for coord, lbl in zip(coordinates,type_figure):
        d = math.sqrt((tp[0] - coord[0])**2 + (tp[1] - coord[1])**2)
        distances.append((d, lbl))
    
    #Sorterar listan efter det första värdet i varje tuple.

    distances.sort(key = lambda x: x[0])
    nearest_nn = distances[ : nn] # Tar ut det 10 närmaste punkterna.

    labels = [lbl for _, lbl in nearest_nn] # Skapar en lista med bara typer av pokemon (ex: 1, 0 , 1, 1)
    pikachu_count = labels.count(1)
    pichu_count = labels.count(0)

    # Finns det fler Pikachu i nn så läggs läggs testpunkter i test_x2 och test_y2

    if pikachu_count > pichu_count: 
        test_x2.append(tp[0])
        test_y2.append(tp[1])
    else:
        test_x1.append(tp[0])
        test_y1.append(tp[1])
        
ui = None

while True:
    try:
        uix = input("Input a X-coordnate or press q + enter to exit. ") # UIX = User input X
        if uix.lower() == "q":
            break
        uix = float(uix)
    

        uiy = (input("Input a Y-coordinate or press q + enter to exit. ")) # UIY = User input Y
        if uiy.lower() == "q":
            break
        uiy = float(uiy)
        
        ui = (uix, uiy) # UI = User input

        if uix < 0 or uiy < 0:
            print("The numbers have to be positive, please try again.")
            continue
        else:
            nn = 10

            # Beräknar euklidiskt avstånd mellan user input ui och träningspunkterna coord.

            distances = []
            for coord, lbl in zip(coordinates, type_figure):
                d = math.sqrt((ui[0] - coord[0])**2 + (ui[1] - coord[1])**2)
                distances.append((d, lbl))
    
            #Sorterar listan efter det första värdet i varje tuple.
   
            distances.sort(key=lambda x: x[0])
            nearest_knn = distances[:nn] # Tar ut det 10 närmaste punkterna.

            vote_1 = sum(lbl for _, lbl in nearest_knn) # Räknar ut hur många av nn som är Pikachu
            vote_0 = nn - vote_1
            if vote_1 > vote_0:
                nearest_label = 1
            elif vote_0 > vote_1:
                nearest_label = 0
            else:
                nearest_label = nearest_knn[0][1]
            
            
            if nearest_label == 1:
                print(f"Coordinate {ui} is classified as Pikachu")
            else:
                print(f"Coordinate {ui} is classified as Pichu")
        break
    except ValueError:
        print("Wrong input, only use numbers, ex: 25.")


plt.figure(dpi= 200)
plt.scatter(xs,ys, c = type_figure, cmap= "bwr")
plt.scatter(test_x1, test_y1, marker='*', s=200, label="Pichu")
plt.scatter(test_x2, test_y2, marker="*", s= 200, label= "Pikachu")

# Plottar ui med en label

if ui is not None:
    plt.scatter(ui[0],ui[1], marker= "^", s = 150, label = "User Input")
    text_label = " User input is Pikachu" if nearest_label == 1 else "User input is Pichu"
    plt.text(ui[0] + 0.3, ui[1] + 0.3, text_label, fontsize = 9, color = "black",)
plt.title("Pikachu vs Pichu")
plt.xlabel("Width")
plt.ylabel("Height")
plt.legend()
plt.show()

