# Project #2
# Hwansu Kim
# 10/03/21

# This program takes an input for the number of customers and outputs the required amount of batches of brownies,
# the containers of ingredients required, and the total cost of the ingredients into a grocery list.


# Constants (Single batch information)
BROWNIES_PER_BATCH = 24
SERVINGS_PER_BATCH = 12


# Constants (Weight and volume conversions)
GRAMS_PER_OUNCE = 28.3495231
OUNCES_PER_POUND = 16

OUNCES_PER_CUP = 8
TSP_PER_CUP = 48

TSP_PER_TBSP = 3


# Constants (Amount of ingredients per batch)
COCOA_GRAMS = 106
SALT_GRAMS = 6

BAKING_POW_GRAMS = 5
ESPRESSO_GRAMS = 2

SUGAR_GRAMS = 447
FLOUR_GRAMS = 180

CHOC_CHIP_GRAMS = 340
BUTTER_POUNDS = .5

VANILLA_TBSP = 1
EGG_WHOLE = 4


# Constants (Amount per container)
COCOA_CON_OUNCES = 8
SALT_CON_OUNCES = 26

BAKING_POW_CON_OUNCES = 8.1
ESPRESSO_CON_OUNCES = 7.05

SUGAR_CON_POUNDS = 4
FLOUR_CON_POUNDS = 5

CHOC_CHIP_CON_OUNCES = 12
BUTTER_CON_POUNDS = 1

VANILLA_CON_OUNCES = 2
EGG_CON = 18


# Constants (Prices for a single container)
COCOA_PRICE = 1.99
SALT_PRICE = .49

BAKING_POW_PRICE = 1.89
ESPRESSO_PRICE = 5.39

SUGAR_PRICE = 1.99
FLOUR_PRICE = 1.99

CHOC_CHIP_PRICE = 1.99
BUTTER_PRICE = 2.99

VANILLA_PRICE = 10.59
EGG_PRICE = 1.99


# Constant (Rounding number; used to round up values to an integer)
ROUNDER = .1


# User input for number of customers.
numCustomers = int(input("How many people to be served? "))


# Equation to retrieve and round up required number of batches based on number of customers.
numBatches = int(numCustomers / SERVINGS_PER_BATCH + (BROWNIES_PER_BATCH - ROUNDER) / BROWNIES_PER_BATCH)


# Equations to retrieve units of ingredients required (Rounded up if number isn't an integer)
cocoaTotal = int(numBatches * COCOA_GRAMS / GRAMS_PER_OUNCE / COCOA_CON_OUNCES + (COCOA_GRAMS - ROUNDER) / COCOA_GRAMS)
saltTotal = int(numBatches * SALT_GRAMS / GRAMS_PER_OUNCE / SALT_CON_OUNCES + ((SALT_CON_OUNCES * GRAMS_PER_OUNCE - ROUNDER) / (SALT_CON_OUNCES * GRAMS_PER_OUNCE)))

bakingPowderTotal = int(numBatches * BAKING_POW_GRAMS / GRAMS_PER_OUNCE / BAKING_POW_CON_OUNCES + ((BAKING_POW_CON_OUNCES * GRAMS_PER_OUNCE - ROUNDER) / (BAKING_POW_CON_OUNCES * GRAMS_PER_OUNCE)))
espressoTotal = int(numBatches * ESPRESSO_GRAMS / GRAMS_PER_OUNCE / ESPRESSO_CON_OUNCES + ((ESPRESSO_CON_OUNCES * GRAMS_PER_OUNCE - ROUNDER) / (ESPRESSO_CON_OUNCES * GRAMS_PER_OUNCE)))

sugarTotal = int(numBatches * SUGAR_GRAMS / (GRAMS_PER_OUNCE * OUNCES_PER_POUND) / SUGAR_CON_POUNDS + (SUGAR_GRAMS - ROUNDER) / SUGAR_GRAMS)
flourTotal = int(numBatches * FLOUR_GRAMS / (GRAMS_PER_OUNCE * OUNCES_PER_POUND) / FLOUR_CON_POUNDS + (FLOUR_GRAMS - ROUNDER) / FLOUR_GRAMS)

chocChipTotal = int(numBatches * CHOC_CHIP_GRAMS / GRAMS_PER_OUNCE / CHOC_CHIP_CON_OUNCES + (CHOC_CHIP_GRAMS - ROUNDER) / CHOC_CHIP_GRAMS)
butterTotal = int(numBatches * BUTTER_POUNDS / BUTTER_CON_POUNDS + (BUTTER_POUNDS - ROUNDER) / BUTTER_POUNDS)

vanillaTotal = int(numBatches * VANILLA_TBSP / (TSP_PER_CUP / TSP_PER_TBSP / OUNCES_PER_CUP) / VANILLA_CON_OUNCES + (VANILLA_TBSP - ROUNDER) / VANILLA_TBSP)
eggTotal = int(numBatches * EGG_WHOLE / EGG_CON + (EGG_WHOLE - ROUNDER) / EGG_WHOLE)


# Output formatted as a grocery list.
print("\nTo serve", numCustomers, "make", numBatches, "batches\n")

print("-" * 30)
print(format("Grocery List", ">21s"))
print("-" * 30)

print(format("Cocoa", "<28s"), cocoaTotal)
print(format("Salt", "<28s"), saltTotal)

print("Baking Powder", format(bakingPowderTotal, "16,d"))
print("Espresso Powder", format(espressoTotal, "14,d"))

print("Sugar", format(sugarTotal, "24,d"))
print("Flour", format(flourTotal, "24,d"))

print("Chocolate Chips", format(chocChipTotal, "14,d"))
print("Butter", format(butterTotal, "23,d"))

print("Vanilla Extract", format(vanillaTotal, "14,d"))
print("Eggs", format(eggTotal, "25,d"))

print("\nTotal price $", format(cocoaTotal * COCOA_PRICE + saltTotal * SALT_PRICE + bakingPowderTotal * BAKING_POW_PRICE + espressoTotal * ESPRESSO_PRICE + sugarTotal * SUGAR_PRICE + flourTotal * FLOUR_PRICE + chocChipTotal * CHOC_CHIP_PRICE + butterTotal * BUTTER_PRICE + vanillaTotal * VANILLA_PRICE + eggTotal * EGG_PRICE, "16,.2f"))


# Versions/Changelog

# v.01: Created input based variable for the number of customers along with a variable for the number of batches
#       based on number of customers. Equation was not accurate enough to round up float numbers to an integer
#       properly; used (+ 0.5) at the end of equation, but this would only round up floats that ended with a
#       decimal place over .5.

# v.02: Changed rounding equation to add .99999 so, regardless of decimal place, the number would round up; except
#       when the number was already an integer. Created a blank grocery list, with no number values, to center and
#       align the banner.

# v.03: Created variables, to retrieve ingredient counts, that held equations based on the number of customers
#       /the number of batches, ingredient information, and appropriate weight and volume conversions;
#       used the same rounding logic on these equations, as I did for the number of batches. Added these
#       variables to the grocery list output section, without formatting, to a print function to test the
#       outputs. After checking accuracy of equations, used int() function to truncate decimal points.
#       Too many "magic numbers" in equations.

# v.04: Created variables for all constants at the top of the program and replaced the "magic numbers" with the
#       corresponding constant variable. Code became a lot more readable. Also created a rounding equation that uses
#       constant variables to achieve the same effect as just simply adding .99999; this was done to ensure there
#       are no "magic numbers".

# v.05: Created print functions for all the ingredients in the grocery list. formatted ingredient count to align
#       to the left of the grocery list. Also added newline escape character in certain places to create
#       breathing room for the entire program's output.

# v1.0: Created print function to display the total price of the grocery list along with the equation to output
#       the total price based on constant variables for the ingredient prices and the total count of each
#       ingredient, previously acquired. Applied formatting so the price only has two decimal places and properly
#       aligns with the ingredient count, on the left side of the grocery list.

# v1.01: Created more empty line space in between blocks of code, related or not, to make the code easier on
#        the eyes. During testing unrealistically large numbers broke alignment; in response: increased the
#        format spacing. Also added comma to all formatting, in order to make numerical values over four
#        digits more readable.


# Testing

# 1. Tested each ingredient calculation by starting with one (1) customer, to ensure the output for the batch number
#    and the ingredient count would be both one (1). Then input a customer count, that would output the maximum
#    amount of batches a single container of an ingredient could create to ensure the number for the ingredient
#    would still be one (1). Then I increased the batch count by one (1), to test that the ingredient count would
#    increase to two (2). And lastly, I then started multiplying the customer count by 10 each time, to ensure
#    calculations would be correct even at unrealistically large inputs for customers.
#   - Examples:
#               -Input 1 for numCustomers, output 1 batch and 1 container of butter.
#               -Input 12 for numCustomers, output 1 batch and 1 container of butter.
#               -Input 13 for numCustomers, output 2 batches and 1 container of butter.
#               -Input 24 for numCustomers, output 2 batches and 1 container of butter.
#               -Input 25 for numCustomers, output 3 batches and 2 containers of butter. This is accurate since
#                each container of butter can make two batches of brownies, 1 pound per container, .5 pounds for
#                each batch. Also each batch on serves twelve people so, with the twenty-fifth customer, a third
#                batch would have to be made.
#               -Input 240 for numCustomers, output 20 batches and 10 containers of butter.
#               -Input 2400 for numCustomers, output 200 batches and 100 containers of butter.
#               -Input 24000 for numCustomers, output 2000 batches and 1000 containers of butter.

# 2. All inputs, aside from integers, break the entire program. This is intended, hence the int() function.
#   - Examples:
#               -A float/decimal causes a ValueError; this is intended since you can't say you're gonna have .25 of a
#                customer.
#               -Strings, like "Twenty", also cause a ValueError. This is intended because we need a numerical value
#                to be stored in the variable for future calculations in the program.
#               -Numbers with commas, like 1,102, also output a ValueError.

# 3. Large, unrealistic, numbers for the numCustomers input breaks the alignment of the grocery list.
#   - Example: 123456789123456789 customers results in the entire list to become misaligned due too many chars.


# Summary
#    First, I started by creating a bare-bones input and output for the customer number and grocery list; then I ran
# into my first hurdle when it came to rounding up the batch number whenever it output a non-integer value. For this
# I had to genuinely step away from the computer and think about the math: initially, I tried adding .5 to the
# batch equation, but since the int() function truncates, this solution only rounded numbers up if they had a
# decimal value of .5 or higher prior to adding the .5. Then, following this logic, I decided to add a value,
# at the end of the equation, that would round the number up regardless of the decimal value, except for when
# the value is already an integer; example: 2.0 would be 2 after truncation, but 2.001 would be 3 after being truncated.
# Figuring this out earlier in the project led to the other calculations, for the ingredients, to be done much faster.
#    After finishing the coding portion of the project, more or less, I started testing the program to ensure
# the accuracy of the numerical outputs, and the visual attractiveness of the program. I ended up noticing that
# my initial formatting lead the list to be too narrow, so I ended up increasing the space between the ingredient
# name and the required amount; this lead to more breathing room for higher input values before the program started
# to become misaligned. This is one problem I'd like to fix, unrealistically long inputs that break alignment, but
# with what I know at the moment, the only solution I can think of is to increase the format spacing even more;
# unfortunately, this negatively affects the visual quality of the program and there's still a finite limit
# before alignment breaks.
#    This project really tested my brain for finding exact solutions, albeit with math rather than coding, and it
# put even more emphasis, than the last project, on thoroughly analyzing and designing the program before coding it.
# The project was also good practice for getting used to using formatting and designing a basic UI that's visually
# appealing. And for future projects, I'm going to definitely create my math equations on paper first because trying
# to think about the arithmetic while in front of the code was really distracting because my mind was split between
# trying to think of the math equation and thinking about what it looks like in Python.