# Example 1
# First we will request user to add a sentence
string = input('Please enter a sentence: ')
i = 0
res = ''
for i in range(len(string)):
    if not i % 2:
        res = res + string[i].upper() # We want every 2 character to be upper
    else:
        res = res + string[i].lower() # we want the other characters to be lower
print(str(res))

# Example 2
# We will start by setting up the variables
new_string = input("Please enter a string: ")
char_storage = "" #blank string to store all the string's characters
char = 1

for i in new_string.split(): 
    if char != 1:
        char_storage += " "
    if char % 2:
        char_storage += i.lower()
    else:   
        char_storage += i.upper()
    char += 1
print(char_storage)

