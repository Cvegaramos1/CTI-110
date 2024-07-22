#Carlos Vega
#7/21/2024
#PLAB5
#This program simulates a self-checkout machine. 


def show_avail_items(items_dict):
    print("Grocery Item                 Price")
    print('-'*35)
    for key, value in items_dict.items():
        print(f"{key:<28} ${value:.2f}")
        
def show_cart(cart):
    print("The items currently in your cart are:")
    for item in cart:
        print(item)
        
def calc_total(cart, items_cost):
    subtotal = 0
    food_tax_rate = 0.02
    itemized_receipt = []

    for item in cart:
        if item in items_cost:
            subtotal += items_cost[item]
            itemized_receipt.append(f"{item:<28} ${items_cost[item]:.2f}")

    food_tax = subtotal * food_tax_rate
    total = subtotal + food_tax

    print("Grocery Checkout Recepit:")
    print('-'*35)
    for line in itemized_receipt:
        print(line)
    print(f"\nSUBTOTAL:       ${subtotal:>3.2f}")
    print()
    print(f"TAX             ${food_tax:>3.2f}")
    print(f"TOTAL:          ${total:>3.2f}")

    return total

def disperse_change(amount_due, amount_paid):
    change = amount_paid - amount_due 
    change = int(change * 100)
    if change == 0:
        print("No change")
        return
    
    print(f"\nThe change owed to you is ${change:.2f}")
    print()
    print("Dispensing...")
    print()

    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickels = change // 5
    change = change - (num_nickels * 5)

    num_pennies = change // 1

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
            
    if num_nickels > 0:
        print(num_nickels, end=' ')
        if num_nickels == 1:
            print("Nickel")
        else:
            print("Nickels")
            
    if num_pennies > 0:
        print(num_pennies, end=' ')
        if num_pennies == 1:
            print("Penny")
        else:
            print("Pennies")
        
items = {
    "apples": 3.69,
    "berries": 4.00,
    "chocolate": 2.89,
    "turkey": 6.99,
    "cheese": 4.00,
    "pepsi": 7.89,
    "eggs": 3.50,
    "bread": 3.00
}
show_avail_items(items)
print('-'*35)
print()
print("*Welcome to the Grocery checkout*")
print()

cart = []

keep_going = "yes"
while keep_going.lower() != "end":
    keep_going = input("Enter an item to add to the cart or type 'end' to stop adding items: ")
    if keep_going.lower() in items:
        cart.append(keep_going.lower())
    elif keep_going.lower() != "end":
        print("That item is not in stock.")
        print()
print()
show_cart(cart)
print()

total_cost = calc_total(cart, items)
print(f"\nYou owe ${total_cost:.2f} for the groceries")

amount_paid = float(input("\nHow much cash will you put in the self-checkout machine? $"))
disperse_change(total_cost, amount_paid)

