# Your function definition goes here

def fibonacci(n):
    num1 = 1
    num2 = 1
    count = 0
    while count < n:
        print(num1)
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        count += 1




n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here
fibonacci(n)