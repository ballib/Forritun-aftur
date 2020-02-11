def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("Input the length of Fibonacci sequence (n>=1): "))

if n <= 0:
    print('enter positive')
else:
    for i in range(1, n+1):
        print(fibo(i), end=' ')