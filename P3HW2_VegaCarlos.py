# Carlos Vega

# 7/9/2024

# P3HW2

# This program will calculate an employee's pay


name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print("-"*37)
print("Employee name:  ",name,"\n")

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    reg_pay = 40 * pay_rate
    gross_pay = reg_pay + overtime_pay
    
else:
    overtime_hours = 0
    overtime_pay = 0
    reg_pay = pay_rate * hours_worked
    gross_pay = reg_pay

print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
print("-"*90)
print(f'{hours_worked:<15}{pay_rate:<12}{overtime_hours:<12}{overtime_pay:<20}{"$"}{reg_pay:<20.2f}{"$"}{gross_pay:.2f}')
