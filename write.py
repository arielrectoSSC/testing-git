import re
import sys

#Print Output
print("Hello, Python! \n How are you doing?")


#Syntax Indentation
if 5>2:
    print("Five is greater than two!")
    




#Variables
w=3.14
x=5 
y="Time to say, 'Hello, World!'"
z=True


# Concatination
print(str(x)+ "  " + y) #numeric values must be converted to string before concatenation
print("It's", x,"o'clock!",y) #mix of numeric and string values

# Other Python Output Methods
print(5+3)
print(245*2)

# W3: Print "I am" and the number 25
print("I am",25)

#Comment
"""This
is
a
comment"""

#Self Assessment including Variable Casting and cases declaring multi-named variables
"""
Instructions: Write a Python program that asks the user for their name,
birth year, and marital status. The program should then calculate the user's age and
print a message that includes their name, age, and marital status.
"""

simpleMessage = "this is Written in Python."
SimpleMessage = "This is Written in Python."
simple_message = "_This is Written in Python._"

welcome_message = [simpleMessage, SimpleMessage, simple_message]
print("\n \n" + welcome_message[1])

Regx = "^[a-zA-Z]+$"
Reg_count = "^[0-9]*$"

name = input("\n What is your name? ")
while not re.match(Regx, name):
    print("Invalid name. Please enter a valid name.")
    name = input("What is your name? ")
    
    
birth_year = input("What is your birth year? ") 
while not re.match(Reg_count, birth_year):
    print("Invalid birth year. Please enter a valid year.")
    birth_year = input("What is your birth year? ")
age=int(2024)-int(birth_year)


marital_status = input("Marital Status? [M]arried, [S]ingle, [D]ivorced, [W]idowed: ")
while not marital_status in ["M", "S", "D", "W"]:
    print("Invalid marital status. Please enter M, S, D, or W.")
    marital_status = input("Marital Status? [M]arried, [S]ingle, [D]ivorced, [W]idowed: ")
    
marital_status = marital_status.upper()

if marital_status == "M":
    spouse_name = input("What is your spouse's name? ")
    while not re.match(Regx, spouse_name):
        print("Invalid spouse name. Please enter a valid name.")
        spouse_name = input("What is your spouse's name? ")
    if re.match(Regx, spouse_name):
        current_status = " You are married to " + spouse_name + "."
elif marital_status == "S":
    current_status = " You are single."  
    
elif marital_status == "D":
    divorce_count = input("How many times have you been divorced? ")
    while not re.match(Reg_count, divorce_count):  
        print("Invalid input. Please enter a valid number.")
        divorce_count = input("How many times have you been divorced? ")
    if divorce_count < 5:
        current_status = " You are divorced." + str(divorce_count) + " times."
    else:
        current_status = "You have lots of divorces. I hope you are well."
        
elif marital_status == "W":
    date_of_death = input("When did your spouse pass away? (YYYY):")
    while not re.match(Reg_count, date_of_death):  
        print("Invalid input. Please enter a valid year.")
        date_of_death = input("When did your spouse pass away? (YYYY):")
    current_status = " We are sorry to hear from you that You are widowed since " + date_of_death + "."

print("Hello2, " + name + "! You are " + str(age) + " years old."+ current_status)
