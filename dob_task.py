

# First of all we will create program that will open a text file DOB.txt

full_name = []
day_birth = []
with open('DOB.txt', 'r') as f:
    for line in f:
        if line.strip(): # This will make for Names to be printed separately from the Birthdate
            data = line.split(' ') # split option will be used for telling how we want to separate the strings
            name = ' '.join(data[0:2]) # I did it by myself 0:2 because we want the name and the surname 2 will not be included we need to fields in this one
            birth_date = ' '.join(data[2:6]) # 2:6 because we want to inculed date, month and year index 6 will not be included but we need 3 fields for this
            full_name.append(name) # This has been added as part of the feedback from previous submission
            day_birth.append(birth_date)  # This has been added as part of the feedback from previous update we used join option and append function also
            print('Name') # we ask this for printing the name of the column as Name
            for name in full_name:
                print(name)
            print('Birthdate') # we ask this to print as the name of the secon column
            for birth_date in day_birth:
                print(birth_date)
