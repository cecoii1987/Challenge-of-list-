# We will import math library
import math

# Input: ask user to add the lengths of the 3 sides of the triagle
# We will create 3 variables
side1 = float(input('Please add the length of 1st side of triangle: '))
side2 = float(input('Please add the length of 2nd side of triangle: '))
side3 = float(input('Please add the length of 3rd side of triangle: '))

# We will calculate the area of a triangle using Heron's formula
# We will define a new variable called s semi-perimeter
s = (side1 + side2 + side3)/2
# And then we will use the area formula
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
print(area)


