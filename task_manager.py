#################################################################################################
'''
Capstone Project Task 1
a. Create functions: reg_user, add_task, view_all and view_mine based on an existing code.
b. Modify reg_user function according to the task instructions.
c. Add more functionality to 'vm' selection option according to the task instructions.
d. Add menu option to generate reports according to the task instructions.
e. Modify menu option to display statistics to the admin according to the task instructions.
'''
#################################################################################################
# Notes:
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import task_manager_lib as t_mgr

# do the login and to create a new user login data
curr_user = t_mgr.fn_login()


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    # print input menu and if admin user, then display extra menu option gr - Generate reports
    menu = input(t_mgr.print_input_menu(curr_user)).lower()

    if menu == 'r':
        '''Add a new user to the user.txt file'''
        t_mgr.reg_user()


    elif menu == 'a':
        '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
        if t_mgr.add_task() == 0:
            continue

    elif menu == 'va':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''
        t_mgr.view_all()

    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        all_tasks = 0  # 0 - print all tasks
        my_tasks = t_mgr.view_mine(curr_user, all_tasks)
        choice = input("Enter the \033[92m task number \033[00m to edit the task "
                       "or type \033[92m -1 \033[00m o return to main menu: ")
        while (int(choice)):
            if (choice == "-1"):
                break
            else:
                for tks in my_tasks:
                    if(choice == tks):
                        t_mgr.view_mine(curr_user, choice)
            break

    
    elif menu == 'ds' and curr_user == 'admin':
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        t_mgr.disp_stat()

    elif menu == 'gr' and curr_user == 'admin':
        "Display reports for the admin user"
        t_mgr.disp_report()


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("\033[31mYou have made a wrong choice, Please Try again\033[00m")
