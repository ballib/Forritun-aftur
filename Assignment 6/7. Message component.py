component_width_int = int(input('Input component width: '))
component_height_int = int(input('Input component height: '))
border_width = int(input('Input border width: '))
border_char = input('Input a border character: ')
message_str = input('Input a message to display: ')

count = 0

a = round(component_height_int/2)
b = round(component_width_int/2)

if len(message_str) > component_width_int:
    message_str = message_str[:component_width_int]


for x in range(component_height_int):
    for y in range(component_width_int):
        if x < border_width:
            print(border_char, end=" ")
        elif x >= component_height_int - border_width:
            print(border_char, end=" ")
        elif y < border_width:
            print(border_char, end=" ")
        elif y >= component_width_int - border_width:
            print(border_char, end=" ")
        else:

            if x+1 == a and y+1 == b:

                for o in message_str.strip():

                    print(o, end=" ")
                count += 1
            else:
                print(" ", end=" ")
    print()
