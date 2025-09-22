for i in range(10):
    print(f"6 x {i} = {6 * i}", end=" ")






i1 = int(input("Choose start of table. "))
i2 = int(input("Choose end of table. "))

for i1 in range(0,12):
    for i2 in range(0,12):
        print(f"{i1} x {i2} = {i1 * i2}", end=" ")