#Here we will create 2 variables num_students and student_register 
# num_student will request the user to add how many students are registering 
#The input will be as a string but we want number so we will use int function

num_students = int(input('Please enter the number of students that are registering: \n'))
student_register = ''

with open('reg_form.txt', 'w') as student_register:
    for student in range(1, (num_students + 1)):
        student_number = input(f'Student {student} ID number: ')
        student_register.write(f'{student_number} .....\n') # we added the dots inside the function because after each registration number task asks for dots to be added
        
        
