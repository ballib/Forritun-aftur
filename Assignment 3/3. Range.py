lower_int = int(input('Input lower: ')) # Do not change this line
upper_int = int(input('Input upper: ')) # Do not change this line
step_int = int(input('Input step size: ')) # Do not change this line

if lower_int < upper_int: # Fill in the missing code below
    print(lower_int)
    while (lower_int + step_int) < upper_int:

        new_num = lower_int + step_int
        lower_int += step_int
        print(new_num)
