NORTH = "n"
SOUTH = "s"
EAST = "e"
WEST = "w"

def parse_input(input_str):
    global row_int
    global col_int
    global at_destination_bool

    input_str = input_str.lower()
    if input_str == NORTH:
        row_int -= 1
    elif input_str == SOUTH:
        row_int += 1
    elif input_str == EAST:
        col_int += 1
    elif input_str == WEST:
        col_int -= 1

    at_destination_bool = is_at_destination(col_int, row_int)



def is_at_destination(col, row):
    if (col, row) == (1,0) or (col, row) == (1,1) or (col, row) == (2,0) or (col, row) == (2,1) or (col, row) == (1, 3) or (col, row) == (3, 3):
        return True
    elif (col, row) == (5, 0) or (col, row) == (5, 1) or (col, row) == (5, 2) or (col, row) == (5, 3) or (col, row) == (5, 4) or (col, row) == (5, 5):
        return True
    return False




col_int = 0
row_int = 0
at_destination_bool = False



def print_summary():
    print("NORTH:")
    print("SOUTH:")
    print("EAST:")
    print("WEST:")
    print("INVALID:")
    print("TOTAL:")



def print_location():
    print(f'You are located at ({col_int}, {row_int})')

def main():
    while not at_destination_bool:
        input_str = input("Enter direction: ")
        parse_input(input_str)
        print_location()
    else:
        print_summary()

main()