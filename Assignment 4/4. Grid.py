num_int = int(input('Input number: ')) # Do not change this line

for y in range(num_int-1, -1, -1):
    for x in range(num_int):
        print(f'({x},{y})', end=" ")
    print()
