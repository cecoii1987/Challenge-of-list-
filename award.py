# Frist of all we will ask user to input the time in minutes spent in each 3 events of triathlon
swimming_time = int(input('Please enter the minutes spent on swimming event: '))
cycling_time = int(input('Please enter the minutes spent on cycling event: '))
running_time = int(input('Please enter the minutes spent on running event: '))

# We will create a new variable called awards that will contain the sum of 3 timings
awards = swimming_time + cycling_time + running_time

# Now we will establish the conditionals in order to determine which award will correspond to each user
if awards <= 100:
    print('Provincial Colours')
elif awards > 100 and awards <= 105:
    print('Provincial Half Colours')
elif awards > 100 and awards <= 110:
    print('Provincial Scroll')
elif awards > 110:
    print('No award')
    
