# We will define the variables
num = 0
count = 0
total = 0

# Then we will calculate the average by using while loop

while num != -1:
    num = int(input('Please enter a number: '))
    if num < 0:
        continue
    total += num
    count += 1
    print(total/count)
