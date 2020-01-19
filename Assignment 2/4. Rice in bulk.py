rice_order_remaining_str = input('Enter the amount of rice to buy (kg): ')  # Do not change this line
soy_sauce_str = input('Enter the amount of soy sauce (bottles): ')  # Do not change this line
# Fill in the missing code below

rice_order_remaining_str = float(rice_order_remaining_str)
soy_sauce_str = float(soy_sauce_str)

first25 = 121
next202 = 78.578


if soy_sauce_str < 10:

    if rice_order_remaining_str < 26:
        total_rice_cost = rice_order_remaining_str * 4.84
        total_soy_cost = soy_sauce_str * 0.99

    elif rice_order_remaining_str <= 45.2 and rice_order_remaining_str > 25:

        total_rice_cost = (rice_order_remaining_str-25) * 3.89
        total_rice_cost = total_rice_cost + (25*4.84)
        total_soy_cost = soy_sauce_str * 0.99
        total_rice_cost = round(total_rice_cost, 3)

    else:
        rice_order_remaining_str = rice_order_remaining_str - 45.2
        total_rice_cost = rice_order_remaining_str * 2.99
        total_rice_cost = total_rice_cost + first25
        total_rice_cost = round(total_rice_cost + next202, 3)
        total_soy_cost = soy_sauce_str * 0.99
else:
    if rice_order_remaining_str < 26:
        total_rice_cost = (rice_order_remaining_str * 4.84)*0.90
        total_soy_cost = soy_sauce_str *0.99

    elif rice_order_remaining_str <= 45.2 and rice_order_remaining_str > 25:

        total_rice_cost = (rice_order_remaining_str - 25) * 3.89
        total_rice_cost = total_rice_cost + (25 * 4.84)
        total_soy_cost = soy_sauce_str * 0.99
        total_rice_cost = round(total_rice_cost, 3)
        total_rice_cost = total_rice_cost*0.90
    else:
        rice_order_remaining_str = rice_order_remaining_str - 45.2
        total_rice_cost = rice_order_remaining_str * 2.99
        total_rice_cost = total_rice_cost + first25
        total_rice_cost = round(total_rice_cost + next202, 3)
        total_rice_cost = total_rice_cost*0.90
        total_soy_cost = soy_sauce_str * 0.99





print('Total price is: $', total_rice_cost + total_soy_cost)  # Do not change this line