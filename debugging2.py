# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

#animal = Lion
# Above line has a syntax error is missing quotations
animal = 'Lion'

animal_type = "cub"

#number_of_teeth = 16
# Above line contains a syntax mistake integer need to be quoted
number_of_teeth = '16'

#full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"
# Above line contains logical and syntax mistake is missing f and the paramenters are added in a wrong manner 
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

#print full_spec
# The above line has a syntax error is missing parnethesis

print(full_spec)
