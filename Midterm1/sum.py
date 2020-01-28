num = 1
sum = 0


while num > 0 and sum <= 100:
    number = input("Input a number: ")
    if number == "q":
        break
    else:
        n = int(number)
        sum += n

print(f'Sum: {sum}')