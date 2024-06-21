# We will have to create a pattern of stars
# We will define 3 variables
rows = 5

# we will start with a for loop and then we will establish some conditions

for i in range(0, rows):
    for j in range(0, i+1):
        print('*', end = ' ')
    print()
for i in range(rows, 0, -1):
    for j in range(0, i-1):
        print('*', end = ' ')
    print()
       
