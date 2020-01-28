balance_float = float(input("Enter initial balance: ")) # Do not change this line
rate_float = float(input("Enter interests (%): ")) # Do not change this line
years_int = int(input("Enter number of years: ")) # Do not change this line


count = balance_float
for x in range(years_int):
    percentage = (rate_float/100) +1

    total_balance = (count * percentage)
    count = total_balance


print(f'Total balance: {round(total_balance,1)}')

