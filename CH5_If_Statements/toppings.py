# Checking for Inequality, !=
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies")

# Resetting
del requested_topping
print('\n')

# Testing Multiple Conditions
# Use a series of simple if statements

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza!")

#Resetting
del requested_toppings
print('\n')

#Checking for Special Items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    #Handle situation if running out of green peppers
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print('Adding ' + requested_topping + '.')

print('\nFinished making your pizza')

##Resetting
del requested_topping
del requested_toppings
print('\n')

#Checking that a List is not Empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + '.')
    print('\nFinished making your pizza.')
else:
    print('Are you sure you want a plain pizza?')