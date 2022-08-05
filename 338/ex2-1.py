# example 2-1. Counting the age by entering the date of birth

name = input("What is your name? ")
birth = int(input("The year you were born? "))

age = 2021 - birth + 1 # korean age
print("%s is %d years old." % (name, age))