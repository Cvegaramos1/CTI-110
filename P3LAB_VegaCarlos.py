# Carlos Vega
# 7/2/2024
# P3LAB
# This program allows the user to enter a money (float) value with
# two places after the decimal that determines change. 

change = float(input("Enter the amount of money as a float: $"))
change = int(change * 100)
print(change)

if change == 0:
    print("No change")
    
num_dollars = change // 100
change = change - (num_dollars * 100)

num_quarters = change // 25
change = change - (num_quarters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickles = change // 5
change = change - (num_nickles * 5)

num_pennies = change // 1

##print(num_dollars)
##print(num_quarters)
##print(num_dimes)
##print(num_nickles)
##print(num_pennies)
if num_dollars > 0:
    print(num_dollars, end=' ')
    if num_dollars == 1:
        print("Dollar")
    else:
        print("Dollars")
        
if num_quarters > 0:        
    print(num_quarters, end=' ')
    if num_quarters == 1:
        print("Quarter")
    else:
        print("Quarters")
        
if num_dimes > 0:
    print(num_dimes, end=' ')
    if num_dimes == 1:
        print("Dime")
    else:
        print("Dimes")
        
if num_nickles > 0:
    print(num_nickles, end=' ')
    if num_nickles == 1:
        print("Nickle")
    else:
        print("Nickles")
        
if num_pennies > 0:
    print(num_pennies, end=' ')
    if num_pennies == 1:
        print("Penny")
    else:
        print("Pennies")
