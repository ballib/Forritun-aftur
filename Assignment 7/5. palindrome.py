# palindrome function definition goes here
def palindrome(in_str):
    new_string = in_str.replace(" ","").replace(".","").replace(",","").replace("'","").replace("!","").lower()

    string_backwards = new_string[::-1]

    if new_string == string_backwards:
        return True
    else:
        return False



in_str = input("Enter a string: ")

if palindrome(in_str):
    print(f'"{in_str}" is a palindrome.')
else:
    print(f'"{in_str}" is not a palindrome.')

# call the function and print out the appropriate message