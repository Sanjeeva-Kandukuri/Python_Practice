# import my_module

print(my_module.greet("Sanjeev"))
print("Value of pi: ", my_module.pi)


# Importing Specific Function
from my_module import greet
print(greet("Jyothi"))

# Using an Alias (shortcut name)

import my_module as m
print(m.greet("Manasa"))

import my_module as pi
print(pi.pi)