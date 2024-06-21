# We will define the variable string_fav
string_fav = input('Please enter the name of your favourite restaurant: ')

# We will create the second variable int_fav
int_fav = int(input('Please add your favourite number: '))

# We will print both statements:
print(string_fav)
print(int_fav)
print(int(string_fav))
# It gives an error because if restaurant name will be a number then it could be converted to integer
# but because the string is a text is not letting to be converted to integer
