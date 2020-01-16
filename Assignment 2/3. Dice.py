d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

if d1 and d2 in range(1,6):
    if d1 + d2 == 2:
        print("Snake eyes")
    elif d1 + d2 == 12:
        print("Dozen")
    else:
        print(d1+d2)
else:
    print("Invalid input")

# Fill in the missing code below