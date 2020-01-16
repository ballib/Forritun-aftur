rice_order_remaining_str = input('Enter the amount of rice to buy (kg): ') # Do not change this line
rice_order_remaining_str = int(rice_order_remaining_str)
soy_sauce_str = int(soy_sauce_str)
if rice_order_remaining_str < 26:
    total_rice_cost = rice_order_remaining_str*4.84
elif rice_order_remaining_str <= 45.2 and rice_order_remaining_str >25:
    total_rice_cost = rice_order_remaining_str*3.89
elif
else:
    total_rice_cost = rice_order_remaining_str*2.99

soy_sauce_str = input('Enter the amount of soy sauce (bottles): ') # Do not change this line
# Fill in the missing code below

if soy_sauce_str < 10:
   total_soy_cost = soy_sauce_str*0.99
else:
    total_rice_cost = total_rice_cost*0.90

print('Total price is: $', total_rice_cost + total_soy_cost) # Do not change this line