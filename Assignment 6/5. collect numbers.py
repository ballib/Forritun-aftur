a_str = input("Input a string: ")


empty_string = ""

for i,c in enumerate(a_str):
    if c.isdigit():
        empty_string += c

    elif a_str[i] == "." and i+1 != len(a_str):
        if a_str[i+1].isdigit():
            empty_string += c

    else:
        if empty_string != "":
            print(empty_string)
            empty_string = ""

