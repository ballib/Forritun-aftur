num_int = int(input('Input number: '))
err_int = int(input('Input accuracy: '))


count = 0
x = num_int/err_int
while True:
    x = (x+num_int/x)/2

    if count == x:
        break
    count = x
x = round(x,err_int)
print(f"The square root of {num_int} is {x}")

