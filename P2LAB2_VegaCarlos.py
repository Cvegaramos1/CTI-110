# Carlos Vega
# 6/27/2024
# P2LAB2
# program that creates a dictionary where the key and value pairs 

cars = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}
keys = cars.keys()
print(keys)
print()
car_input = input("Enter a vehicle to see it's mpg: ")
print()
mpg_output = cars[car_input]
print(f'The {car_input} gets {mpg_output} mpg.\n')
distance = float(input(f'How many miles will you drive the {car_input}? '))
print()
gallons = distance/ mpg_output
print(f'{gallons:.2f} gallon(s) of gas are needed to drive the {car_input} {mpg_output:.1f} miles. ')
