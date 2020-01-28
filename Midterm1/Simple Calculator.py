num = int(input("Input number: "))

operator = str(input("Input operation: "))

num2 = int(input("Input number: "))

if operator == "+":
    total = num + num2

elif operator == "-":
    total = num - num2

elif operator == "*":
    total = num * num2

elif operator == "/":
    total = num / num2
else:
    total = None

if total != None:
    print(f'{num} {operator} {num2} = {round(total)}')
else:
    print(f'{num} {operator} {num2} = {None}')