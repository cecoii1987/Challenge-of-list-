# For this task is asking to ask user to add 3 integers and then we will make operations
# with those integers that user input

# For that we will use 3 variables num1, num2, num3
num1 = int(input('Please enter the first number: '))
num2 = int(input('Please enter the second number: '))
num3 = int(input('Please enter the third number: '))

# Then we will print out operation made up with the integers inputed by the user
# Firs output requested is the sum of the 3 numbers
print(num1 + num2 + num3)
# Second ouput is multiplication between num3 and num1
print(num3*num1)
# And the third is a math expression in which we sum the 3 numbers and divide by num3
print((num1 + num2 +num3)/num3)
