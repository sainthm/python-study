# example 2-2. An annotation

"""

Output data using print() functions
- Writer: sainthm
- Date: 2022.08.05

"""

'''

However, you can use 
three quotes.

'''

name = input("What is your name? ") # variable name

# variable birth: the year of birth 
birth = int(input("The year you were born? "))

age = 2021 - birth + 1 # korean age ## variable age
print("%s is %d years old." % (name, age))