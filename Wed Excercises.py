# Input Prompt:
# Write a program that takes the user's name as input and prints a personalized greeting.

def greet():
     name = input("Please enter your name")
     print(f"Greetings, {name}!")
greet()

# Numeric Input:
# Create a program that asks the user to enter two numbers and calculates their sum.

def add(num1, num2):
    return num1 + num2
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
print(number_1, "+", number_2, "=",
					add(number_1, number_2))

# Favorite Color:
# Prompt the user to enter their favorite color and display a message acknowledging their choice.

# def color():
#      color = input("Please enter a color of your choosing")
#      print(f"Your current favourite color is, {color}! I like {color} too.")
# color()

# Print Multiple Lines:
# Write a program that prints a message on one line, and then on the next line, prints a different message.

# print("This was easier than I thought\n" \
#       "But it would be easier and more fun with other people :) \n")

# Formatted Output:
# Create a program that prints a sentence with placeholders for the user's name and age.

def greet():
     name = input("Please enter your name")
     age = input("Please enter your age")
     print(f"They're name was {name}, and they were {age} years old.")
greet()


# Repeated Output:
# Print the message "Hello" five times using a loop.
# for _ in range(5):print("Hello")
#"range (5)" will output a sequence of "Hello" 5 times, with variables going from 0-4(number count start from 0)

# Variable Swap:
# Swap the values of two variables and print the result.


# Variable Concatenation:
# Concatenate two strings stored in variables and print the combined string.
# string1 = ("Take ")
# string2 = ("a Hike")

# combined = string1 + string2
# print(combined)

# Variable Initialization:
# Declare a variable to store your age and initialize it with your actual age.


# Arithmetic Operations:
# Write a program that takes two numbers as input and performs addition, subtraction, multiplication, and division.
# def add(num1, num2):
#     return num1 + num2

# def subtract(num1, num2):
#     return num1-num2

# def multiply(num1, num2):
#     return num1*num2

# def divide(num1, num2):
#     return num1/num2

# print("Please select the operation -\n" \
# 		"1. Add\n" \
# 		"2. Subtract\n" \
# 		"3. Multiply\n" \
# 		"4. Divide\n")

# select = int(input("Select operations for 1, 2, 3, 4 :"))

# number_1 = int(input("Enter first number: "))
# number_2 = int(input("Enter second number: "))

if select == 1:
	print(number_1, "+", number_2, "=",
					add(number_1, number_2))

# elif select == 2:
# 	print(number_1, "-", number_2, "=",
# 					subtract(number_1, number_2))

# elif select == 3:
# 	print(number_1, "*", number_2, "=",
# 					multiply(number_1, number_2))

# elif select == 4:
# 	print(number_1, "/", number_2, "=",
# 					divide(number_1, number_2))
# else:
# 	print("Invalid input")

# Comparison Operators:
# Create a program that compares two numbers and prints whether they are equal or not.
# number_1 = int(input("Enter first number: "))
# number_2 = int(input("Enter second number: "))
# if number_1 == number_2:
# 	print("Given numbers are equal :)")
# else:
# 	print("The numbers you gave were not equal :()")

# String Concatenation:
# Concatenate two strings and print the result.
string1 = ("Nvm, don't ")
string2 = ("take a Hike")

combined = string1 + string2
print(combined)

# If-Else Statement:
# Write a program that takes a user's age as input and prints whether they are eligible to vote or not.
user_age = input("Enter your age: ")
try:
    age = int(user_age)

    if age >= 18:
        print("You may vote :D")
    else:
        print("You cannot vote yet :(")
except ValueError:
    print("Invalid input. Please enter a valid age as a number >:(")

# Nested If Statements:
# Implement a program that checks if a number is positive, negative, or zero.

# Looping Control Flow:
# Use a loop to print the numbers from 1 to 10
    