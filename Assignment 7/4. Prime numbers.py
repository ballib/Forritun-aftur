# is_prime function definition goes here
def is_prime(num):
    for x in range(2, num//2):
        if num % x == 0:
            print(f'{num} is not a prime')
            break

    else:
        print(f'{num} is a prime')




num = int(input("Input an integer greater than 1: "))


is_prime(num)
# Call the function here and print out the appropriate message