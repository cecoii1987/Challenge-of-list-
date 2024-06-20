# First of all we will start with defining the variable str_manip that will contain the input
str_manip = input('Please enter a sentence: \n')

# We will calculate the length of the str_manip
print(len(str_manip))

# we will create a new string which will contain the slicing in which we have to find the last letter
str_manip1 = str_manip[-1]
print(str_manip1)

# Next we will use the replace function in which we will replace each occurence of last letter in the sentence with @
print(str_manip.replace(str_manip1, '@'))
      
# We will print the last 3 charcters in str_manip backwords
print(str_manip[-1:-4:-1])

# Finally we will create for this task a 5 letter word that will contain the first 3 letters and the last 2 characters
print(str_manip[0:3]+str_manip[-2: ])
