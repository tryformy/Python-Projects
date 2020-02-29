# TryForMy
# 2/25/20
# This program will determine compound interest at a set rate of 0.04
# and a set amount of years (20) using an input value from a user.


# Declare variables
deposit = float(input("Enter your deposit amount: "))
rate = 0.04
interest = 0
years = 2018

# To correct the fact the other table starts at 2019, and the compounded value
# is already added to the amount totalled, this simply sets the date to
# 2018 and the initial deposit value for the firs table entry
header = '\n' 'Year \t Amount'
print(header.format('years', 'interest'))
print("---- \t ------")
print(years, "\t", format(deposit, ',.2f'))



# --- Create loop with math here---
# !!! use for loop 1-21, remember rate has to be added by 1 !!!
# This goes through the loop and adds compound interest 20 times and outputs
# values for each year, since our print is in the loop
for year in range(1,21):
    interest = deposit * (rate + 1) ** year
    years = years + 1
    print(years, "\t", format(interest, ',.2f'))


# Total interest earned
print( '\n'
    "Total interest earned:", format(interest - deposit, ',.2f'))
