# Carlos Vega
# 6/22/2024
# P1HW2
# This program calculates and displays travel expenses

print("This program calculates and displays travel expenses")

print()
      
budget = float(input("Enter Budget: "))
print()
destination = input ("Enter your travel destination: ")
print()
gas_expense = float(input ("How much do you think you will spend on gas? "))
print()
hotel_expense = float(input ("Approximately, how much will you need for accomodation/hotel? "))
print()
food_cost = float(input ("Last, how much do you need for food? "))

total_expenses = gas_expense + hotel_expense + food_cost
remainning_budget = budget - total_expenses

print()
print()

print("------------Travel Expenses------------")

print(f"Location: {destination} ")
print(f"Initial Budget: {budget} ")

print()

print(f"Fuel: {gas_expense} ")
print(f"Accomodation: {hotel_expense} ")
print(f"Food: {food_cost} ")

print()

print(f"Remaining Balance: {remainning_budget} ")
