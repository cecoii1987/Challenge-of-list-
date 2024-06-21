# We will have to create a pattern of stars
# We will define variables
i = 0
stars = '*' 
index = 0
#Then we will create a for loop with conditionals
for i in range(1, 10):
    if i == 1:
        print(stars)
    elif i < 5:
        stars = stars + '*'
        print(stars)
    elif i == 5:
        print(stars +'*')
    elif i > 5 < 10:
        index = 10 - i
        print(stars[0:index])
       
