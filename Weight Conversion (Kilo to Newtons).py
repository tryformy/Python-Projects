# Given a mass entered in kilograms, calculate the corresponding weight in newtons.
# using the formula weight = mass * 9.8
# TryForMy
# 2/14/2020

#Declare named constants
CONVERSION_FACTOR = 9.8
MINIMUM_WEIGHT = 100
MAXIMUM_WEIGHT = 500



# Prompt a user to enter mass in kilograms
mass = float(input("Enter the mass of an object (Kilograms): "))


# Calculate the weight in newtons
weight = mass * CONVERSION_FACTOR



# Display the weight in newtons, and whether the object is too heavy, or too light.
# If the calculated weight is less than 100 newtons, print a message that it is
# too light. If the calculated weight is more than 500 newtons, print a message
# that it is too heavy. Otherwise just print the weight it newtons.
if weight < MINIMUM_WEIGHT:
    print("The object is too light. The weight is", format(weight, ".1f"), "newtons")
elif weight > MAXIMUM_WEIGHT:
    print("The object is too heavy. The weight is", format(weight, ",.1f"), "newtons")
else:
    print("The weight is", format(weight, ".1f"), "newtons")
