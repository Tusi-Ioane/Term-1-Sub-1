# #code for monday exercise 1 - basic calculator
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

# if select == 1:
# 	print(number_1, "+", number_2, "=",
# 					add(number_1, number_2))

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


# #code for monday exercise2 - odd or even
# def num(): (input("Enter any number to test whether it is odd or even:"))
# if (num% 2) == 0: print("The number is even")
# else: print ("The number is odd")
# num()


#code for monday exercise3 - age
# Get user input for age
user_age = input("Enter your age: ")
try:
    age = int(user_age)

    if age >= 18:
        print("You may vote :D")
    else:
        print("You cannot vote yet :()")
except ValueError:
    print("Invalid input. Please enter a valid age as a number >:()")


#code for monday exercise - explanation
a = 5 * 2 + 3
print("a = 13")
# * = multiply, + = addition. 
#Taking the above values into account "5 * 2 + 3" is equal to "5 x 2 + 3" which equals 13, making "a" equal to 13 :)