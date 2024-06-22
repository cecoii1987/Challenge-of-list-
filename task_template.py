# We imported date time
import datetime


# First we start by defining functions
# Function 1: reg_user is called when the user selects 'r' to register a user.

def register_user():
    new_username = input('Please enter a new username: \n')
    new_password = input('Please enter a new password: \n')
    pass_confirm = input('Please confirm your new password: \n')
    while new_password != pass_confirm:
        print('Your confirmed password does not match the original' +
              'password.')
        new_password = input('Please enter your new password: \n')
        pass_confirm = input('Please confirm your new password: \n')
        if new_password == pass_confirm:
            password_list.append(new_password)
            username_list.append(new_username)
    with open(file1, 'a') as f:
        f.write(f'\n{new_username}, {pass_confirm}')

# Function 2: add_task is called when a user selects 'a' to add a new task.
# For this task we will use datetime that we will import
# And also we will give format to the dates


def add_task():
    name = input('Please enter the username of the person you wish to' +
                 'assign the task to: \n')
    title = input('Please enter the title of the task: \n')
    description = input('Please enter the description of the task: \n')
    current_date = datetime.date.today()
    assigned_date = current_date.strftime('%d %b %Y')
    date_format = input('Please enter the date of the task' +
                        '(e.g. dd-mm-yyyy): \n')
    date_list = date_format.split('-')
    numbers_date = [int(x) for x in date_list]
    due_date = datetime.date(numbers_date[2], numbers_date[1], +
                             numbers_date[0]).strftime('%d %b %Y')
    task_completed = 'No'
    task_list = [name, title, description, assigned_date, due_date,
                 task_completed]
    count = 0
    tasks_dict = {}
    tasks_dict[f'Task {count} details: '] = task_list
    with open(file, 'a') as f:
        for key in tasks_dict:
            line_string = str(tasks_dict[key])
            bad_chars = ['[', ']', '\'']
        for i in bad_chars:
            line_string = (line_string.replace(i, ''))
        f.write(f'{line_string} \n')
    return 'Your new task has been added successfully.'

# Function 3: view_all is called when a user selects 'va' to view all tasks
# listed in tasks.txt.
# These tasks are already stored in the dictionary 'tasks_dict'.
# Therefore, the dictionary will be used to view all the tasks.


def view_all():
    task_count = 0
    with open(file, 'r') as f:
        data = f.readlines()
        print(data[0])
        for task in data:
            task = task.split(', ')
            task_count += 1
            print(f'''----------------------------
Task {task_count}:       {(task[1])}
Assigned to:             {(task[0])}
Date assigned:           {(task[3])}
Due Date:                {(task[4])}
Task Complete?           {(task[5])}
Task Description:
 {(task[2])}
#  -----------------------------------------------''')
#     return 'End of tasks.'

# Function 4: view_mine is called when a user selects 'vm' to view all tasks
# assigned to them.


def view_mine():
    task_count = 0
    tasks_dict = {}
    for key in tasks_dict:
        task_count += 1
        if usernames == (tasks_dict[key][0]):
            print(f'''______________________
Task {str(task_count)}:    \t{str(tasks_dict[key][1])}
Assigned to:                 {str(tasks_dict[key][0])}
Date Assigned:               {str(tasks_dict[key][3])}
Due Date:                    {str(tasks_dict[key][4])}
Task Complete?               {str(tasks_dict[key][5])}
Task Description:
 {str(tasks_dict[key][2])}
___________________________________________________''')
    return 'This are tasks assigned to you.'

# We added the txt file into variables


file = 'tasks.txt'
file1 = 'user.txt'

# =====importing libraries===========
'''This is the section where you will import libraries'''

# ====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and
      passwords from the file
    - Use a while loop to validate your user name and password
'''
# We start by asking the username to log in
# And we go through validation of the password
# We will use append option here to make sure the details entered are appended
# to file doc

username_list = []
password_list = []
with open(file1, 'r') as f:
    for line in f:
        line = line.strip()
        usernames, passwords = line.split(', ')
        username_list.append(usernames)
        password_list.append(passwords)
login_username = input('Please enter your username: \n')
login_password = input('Please enter your password: \n')
if login_username not in username_list:
    login_username = input('Please enter your username again: \n')
if login_password not in password_list:
    login_password = input('Please enter your password again: \n')
if login_password in password_list:
    pass_confirm = input('Please confirm you password: \n')
    if login_password == pass_confirm:
        print('Successful password.')
    else:
        print('The password or username are incorrect please try again.')
print('Congratulations for logging in!')
while True:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r':
        register_user()
        pass
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''

    elif menu == 'a':
        add_task()
        pass
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following:
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not
              complete.'''
    elif menu == 'va':
        view_all()
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in
              the PDF
            - It is much easier to read a file using a for loop.'''

    elif menu == 'vm':
        view_mine()
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as
              the username you have read from the file.
            - If they are the same you print the task in the format of
              Output 2 shown in the PDF '''

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")
