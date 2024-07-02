# Carlos Vega

# Date6/27/2024

# P2HW1

# This program calculates and displays travel expenses

print("This program calculates and displays travel expenses\n")

budget = float(input("Enter Budget: "))
print()

location = input("Enter your travel destination: ")

print()
fuel = float(input("How much do you think you will spend on gas? "))

print()

hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()

food = float(input("Last, how much do you need for food? "))

expenses = fuel + hotel+ food

remainAmount = budget - expenses

print(11*"-","Travel Expenses",11*"-")
print(f'{"Location:":<20}{location}')
print(f'{"Initial Budget:":<20}${budget:.2f}')
print(f'{"Fuel:":<20}${fuel:.2f}')
print(f'{"Accomodation:":<20}${hotel:.2f}')
print(f'{"Food:":<20}${food:.2f}')
print(40*"-")
print()
print(f'{"Remaining Balance:":<20}${remainAmount:.2f}')




