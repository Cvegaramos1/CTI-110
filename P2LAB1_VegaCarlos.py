# Carlos Vega
# 6/25/2024
# P2LAB1
# Assignment tests student's knowledge of how to write code that
# performs mathematical calculations and displays information to users

import math

radius = float(input(" What is the radius of the circle? "))
print()
diameter = 2 * radius
circumference = 2 * radius * math.pi
area = math.pi * radius**2
print(f'The diameter of the circle is {diameter:.1f}\n')
print(f'The circumference of the circle is {circumference:.2f}\n')
print(f'The area of the circle is {area:.3f}\n')
