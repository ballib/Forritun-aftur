import math

x1_str = input("Input x1: ") # do not change this line
y1_str = input("Input y1: ") # do not change this line
z1_str = input("Input z1: ") # do not change this line
x2_str = input("Input x2: ") # do not change this line
y2_str = input("Input y2: ") # do not change this line
z2_str = input("Input z2: ") # do not change this line

x1 = int(x1_str)
y1 = int(y1_str)
z1 = int(z1_str)
x2 = int(x2_str)
y2 = int(y2_str)
z2 = int(z2_str)
# convert strings to ints
d = math.sqrt(((x1-x2)**2) + ((y1-y2)**2) + ((z1-z2)**2))
#  d =
print("d =",d)  # do not change this line