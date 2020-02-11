# The function definition goes here

def in_range(num):
    if num > 1 and num < 555:
        return True
    return False

num = int(input("Enter a number: "))

if in_range(num) == True:
    print(f'{num} is in range.')
else:
    print(f'{num} is outside the range!')

# You call the function here