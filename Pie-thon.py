"""
Pie-thon.py

Answers frequently asked questions
"""


import sys
import datetime

option = str(input("""\
Welcome to Pie-thon Pizza recipes! The best pies in the city, located at 25 Broadway!
Here's some frequently asked quesitons:

A) How many slices of pepperoni will I need?
B) How many pizzas do I need to feed 'x' amount of people?
C) How many days until Pie Day?

Choose from the above, type A, B, or C
"""))

print() #space

##  OPTION A  ##
if option == "A" or option == "a":

    pepperoni = int(input("""\

Our ratio is 10 pepperonis to one pizza. How many pizza's are you making?
"""))

    p = 0

    while p <= pepperoni:
        print(f"To make {p:2} pizza, you will need {p*10:3} slices of pepperonis.")
        p += 1
        
##  OPTION B  ##
elif option == "B" or option == "b":

    people = int(input("""\
One pizza can feed around four people. How many people do you have?
"""))

    for ppl in range(0,people+1,1):
        print(f"To feed {ppl} people you would need {round(ppl//4)} pizza.")

##  OPTION C  ##
elif option == "C" or option == "c":
    
    pi = datetime.datetime(2020, 3, 14) - datetime.datetime.today()
    print(f"{pi.days} days until Pie Day!!")

##  NONE OF ABOVE  ##    
else:
    print("Error: you did not press A, B, or C. Goodbye!")
    
sys.exit(0)
