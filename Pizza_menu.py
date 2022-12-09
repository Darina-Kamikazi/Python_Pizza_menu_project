#!usr/bin/env python 3

#   CREATED BY: Darina Kamikazi
#   CREATED ON : Dec 9, 2022
#   PURPOSE: This program creates a menu system that allows users to order pizzas of varying quantities, sizes and toppings 
#   SKILLS USED: user inputs, for loops, if statements

#Prompt: Create a menu system that allows users to order pizzas of varying quantities, sizes and toppings 
num_pizzas = int(input("How many pizzas would you like?: "))

subtotal = 0

#Creating loops for different input responses
for i in range(num_pizzas):
    print(f"For pizza {i + 1}")
    pizza_size = input("What size pizza would you like? (Small, Medium, Large):").lower()
    num_toppings = int (input ("How many toppings would you like?: "))
    extra_sauce = input("Would you like extra sauce for $0.50? (Y/N): ").lower()

    if pizza_size == "small" or pizza_size == "s":
        pizza_cost = 7.00 + 0.50 * num_toppings
        pizza_size == "small"
    elif pizza_size == "medium" or pizza_size == "m":
        pizza_cost = 10.75 + 1.00 * num_toppings
        pizza_size = "medium"
    else: 
        pizza_cost = 14.75 + 1.50 * num_toppings
        pizza_size = "large"

    if extra_sauce == "yes" or extra_sauce == "y":
        print (f" A {pizza_size} pizza with {num_toppings} toppings and extra sauce is ${pizza_cost}")
    else:
        print (f" A {pizza_size} pizza with {num_toppings} toppings is ${pizza_cost}")
    subtotal += pizza_cost
 

# Computing final costs
sales_tax = subtotal * 0.04
total_cost = subtotal + sales_tax

#Final bill output
print (f"Subtotal: ${subtotal}")
print (f"Tax (4%): ${sales_tax}")
print (f"Total: ${total_cost}")
