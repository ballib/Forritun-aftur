a_str = input("Input a float: ")

floated = float(a_str)

rounded = '{0:.2f}'.format(floated)

new_string = str(rounded)
width = 12

print(f'{new_string.rjust(width)}')