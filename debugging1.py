# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# print "Welcome to the error program"
# print "\n"
# Above code has mistakes the print need to be among parenthesis and there is not need to print separate a new line we can do it in one line is a syntax error
print("Welcome to the error program\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
#age_Str == "24 years old" 
#age = int(age_Str) 
#print("I'm" + age + "years old.")
# The above code contain various mistake. One of them is age_Str has double = which is not correct when we set a variable
# Second mistake age cannot run because age_Str is a string not just a number in order to be csted we need to remove the words
# And in the printing part we need to use f
# Syntax error
age_Str = "24" 
age = int(age_Str) 
print(f"I'm {age} years old.")

# Variables declaring additional years and printing the total years of age
# years_from_now = "3"
# total_years = age + years_from_now
# print "The total number of years:" + "answer_years"
# The above code contains syntax error and logical error. We cannot sum numbers with string
# The print option is missing parenthesis and f function
years_from_now = str(input('Please enter years from now: '))
total_years = age + float(years_from_now)
print(f"The total number of years: {total_years}")

# Variable to calculate the total amount of months from the total amount of years and printing the result
#total_months = total * 12
#print "In 3 years and 6 months, I'll be " + total_months + " months old"
# In the above code there are some syntax and logical mistakes. For example the variable total is not defined
# What we need to do is to modify years_from_now variable to input so user can add any age
# Instead of total we will use total_years. And then print option need to have parenthesis

total_months = total_years * 12
print(f"In 3 years and 6 months, I'll be {total_months} months old")

#HINT, 330 months is the correct answer
