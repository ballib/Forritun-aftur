num_float = float(input("Input a decimal: ")) # Do not change this line

# Fill in the missing code below

count = 1
the_fraction = False

while count <= 100:
    if num_float == 1/count:
        the_fraction = True
        break
    count += 1

if the_fraction:
    print(f"The fraction is 1/{count}.")
else:
    print("Fraction not found!")