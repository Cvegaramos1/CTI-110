# Carlos Vega
# 7/3/2024
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

grade_liast =[]
mod_1 = float (input('Enter grade for Module 1: '))
mod_2 = float (input('Enter grade for Module 2: '))
mod_3 = float (input('Enter grade for Module 3: '))
mod_4 = float (input('Enter grade for Module 4: '))
mod_5 = float (input('Enter grade for Module 5: '))
mod_6 = float (input('Enter grade for Module 6: '))

grade_list = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

print()
print(12*"-","Results",12*"-")
lowest = min(grade_list)
highest = max(grade_list)
total = sum(grade_list)
length = len(grade_list)
avg = total/length

print(f'Lowest Grade:       {lowest} ')
print(f'Highest Grade:      {highest} ')
print(f'Sum of Grades:       {total} ')
print(f'Average:            {avg:.2f} ')

print(40*"-")

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
elif avg >= 50:
    print('Your grade is: F')







