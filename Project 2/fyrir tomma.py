cumulative_total = 0
largest_num = 0
even_num = 0
odd_num = 0

num = 1

while num > 0:
    num = int(input('Enter an integer: '))


    if num <= 0:
        break
    else:
        if num > largest_num:
            largest_num = num

        if num % 2 == 0:
            even_num += num
        else:
            odd_num += num
        cumulative_total = num + cumulative_total
        print('Cumulative total:', cumulative_total)

print(largest_num)
print(even_num)
print(odd_num)