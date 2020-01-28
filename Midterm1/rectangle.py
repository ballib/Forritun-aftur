rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))


for x in range(rows):
    for y in range(columns):
        print("*", end=" ")
    print("\n")
