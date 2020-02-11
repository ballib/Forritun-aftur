comp_width = int(input('Input component width: '))
comp_height = int(input('Input component height: '))
border_width = int(input('Input border width: '))
border_char = input('Input a border character: ')
message = input('Input a message to display: ')

# create all strips
strips = [[f"{border_char} "] * comp_height for i in range(comp_width)]

# empty middle section
for i in range(border_width, comp_width - border_width):
    empty = ["  " for i in range(comp_height - (2 * border_width))]
    strips[i][border_width:-border_width] = empty

# text in center
if len(message) > comp_width:
    message = message[:comp_width]
offset = comp_width // 2 - len(message) // 2
for i in range(len(message)):
    cur_y = i + offset
    cur_x = comp_height//2
    if strips[cur_y][cur_x] != f"{border_char} ":
        strips[cur_y][cur_x] = message[i] + " "

# print strips
for i in range(comp_height):
    for j in range(comp_width):
        print(strips[j][i], end="")
    print()