cm_str = input("Input cm: ") # do not change this line

int_inches = round(int(cm_str)/2.54)
inches = int_inches%12
int_feet = int_inches//12
feets = int_feet%3
yards = int_feet//3
print(yards, "yd. ", feets, 'ft.', inches, 'in.') # do not change this line