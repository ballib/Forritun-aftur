MIN = int(input("Enter minimum value: "))
MAX = int(input("Enter maximum value: "))

def position():
    pos = int(input(f'Input a position between {MIN} and {MAX}: '))
    return pos

def first_position(pos):
    count = MIN
    the_string = ""
    for x in range(MIN, MAX+1):
        if count == pos:
            the_string += str("o")
            count += 1
        else:
            the_string += str("x")
            count += 1
    print(the_string)
    return the_string


def mover(pos, letter):
    if letter == "l":
        if pos > MIN:
            pos -= 1
    else:
        if pos < MAX:
            pos +=1
    return pos




def main():
    pos = position()
    first_position(pos)

    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    counter = 1
    while counter > 0:
        letter = input("Input your choice: ")

        if letter != "l" and letter != "r":
            first_position(pos)
            quit()
        else:
            pos = mover(pos, letter)
            first_position(pos)



main()