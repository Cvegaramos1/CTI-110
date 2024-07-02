#Carlos Vega
#6/25/2024
#P2HW2
#This program displays lowest, highest, sum, and average of grades 
grade_list =[]
mod1= float(input("Enter grade for module1: "))
mod2= float(input("Enter grade for module2: "))
mod3= float(input("Enter grade for module3: "))
mod4= float(input("Enter grade for module4: "))
mod5= float(input("Enter grade for module5: "))
mod6= float(input("Enter grade for module6: "))

grade_list = [mod1, mod2, mod3, mod4, mod5, mod6]

print()
print('------------Results------------')
lowest = min(grade_list)
highest =max(grade_list)
total =sum(grade_list)
length =len(grade_list)
average =total/length

print(f"Lowest Grade:       {lowest} ")
print(f"Highest Grade:      {highest} ")
print(f"Sum of Grade:       {total} ")
print(f"Average:            {average:.2f} ")
print('----------------------------------------')

