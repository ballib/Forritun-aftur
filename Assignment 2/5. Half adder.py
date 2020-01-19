a_str = input("Enter value for A: ") # Do not change this line
b_str = input("Enter value for B: ") # Do not change this line

# Fill in the missing code below

a_str = int(a_str)
b_str = int(b_str)

if a_str == 0 and b_str == 0:
    s_bool = 0
    c_bool = 0
elif a_str == 1 and b_str == 0:
    s_bool = 1
    c_bool = 0
elif a_str == 0 and b_str == 1:
    s_bool = 1
    c_bool = 0
else:
    s_bool = 0
    c_bool = 1



print('S={}, C={}'.format(s_bool, c_bool)) # Do not change this line