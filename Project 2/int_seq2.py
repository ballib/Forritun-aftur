num = 1
total = 0
largest_num = 0
even_number = 0
odd_number = 0
while num > 0:
    num = int(input("Enter an integer: "))
    if num <= 0:
        break
    else:
        if num > largest_num:
            largest_num = num
        if num % 2 == 0:
            even_number += num
        else:
            odd_number += num
        total += num
        print(f'Cumulative total: {total}')
if total > 0:
    print(f'Largest number: {largest_num}')
    print(f'Sum of even numbers: {even_number}')
    print(f'Sum of odd numbers: {odd_number}')



