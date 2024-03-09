'''
The functions to be used in Capstone Project Task 1
'''

import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]
    #print(task_data)  # delete after
    #print(task_data[1])
    #d=task_data[1].split(";")
    #print(d)

task_list = []
id = 0
for t_str in task_data:
    curr_t = {}
    id += 1

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['task_id_num'] = str(id)
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")
    print(user_data[0].split(';'))

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

# do the login and to create a new user login data
def fn_login():
    logged_in = False
    while not logged_in:

        print("LOGIN")
        curr_user = input("Username: ")
        curr_pass = input("Password: ")
        if curr_user not in username_password.keys():
            print("User does not exist")
            continue
        elif username_password[curr_user] != curr_pass:
            print("Wrong password")
            continue
        else:
            print("Login Successful!")
            logged_in = True
    return curr_user

# This function is to add a new user
def reg_user():
    # - Request input of a new username
    new_username = input("New Username: ")

    if new_username in username_password.keys():
        print("\033[31m User already exist, Please choose another name\033[00m")
        return 0

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password

        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # - Otherwise you present a relevant message.
    else:
        print("\033[31mPasswords do no match\033[00m")

def add_task():
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return 0
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")

#display all tasks
def view_all():
    for t in task_list:
        disp_str = f"Task {t['task_id_num']}: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)

# display mine task
def view_mine(curr_user,nm_task):
    task_nm = []
    print(task_file)  # delete after
    for t in task_list:
        if t['username'] == curr_user:
            disp_str = f"\033[92m \n Task {t['task_id_num']}:\033[00m \t\t\t {t['title']}\n"
            disp_str += f"\033[92m Assigned to:\033[00m \t\t {t['username']}\n"
            disp_str += f"\033[92m Date Assigned:\033[00m \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"\033[92m Due Date:\033[00m \t\t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"\033[92m Task Description:\033[00m \t {t['description']}\n"
            task_nm.append(t['task_id_num'])
            if(nm_task==0):
                print(disp_str)
            elif(t['task_id_num']==nm_task ):
                print(disp_str)
                new_data = task_data[int(nm_task)-1].split(";")
                if (new_data[5]== "Yes"):
                    print(f"\033[31mThe task {nm_task} cannot be edited it's completed\033[00m")
                    break
                pr_menu("return", "name", "date", "complete")
                in_sel = "0"
                while (in_sel):
                    if not in_sel.isalnum():
                        print("type a number")
                    elif (in_sel == "0"):
                        in_sel = input("Your option:\t").lower()
                    elif (in_sel == "1"):
                        break
                    elif (in_sel == "2"):
                        newName = input("Type a new name:\t").lower()
                        save_data(nm_task, str(newName), "0", "0")
                        in_sel = "0"
                    elif (in_sel == "3"):
                        newDate = input("Type a new date YYYY-MM-DD:\t").lower()
                        save_data(nm_task, "0", newDate, "0")
                        in_sel = "0"
                    elif (in_sel == "4"):
                        newCmpl = input("Mark Y - complete or N - not complete:\t").lower()
                        if(newCmpl == "y"):
                            save_data(nm_task, "0", "0", "Yes")
                        elif(newCmpl == "n"):
                            save_data(nm_task, "0", "0", "No")
                        else:
                            print("\033[31m Try again\033[00m")
                        in_sel = "0"
    #print(task_list)
    return task_nm

# display statistics
def disp_stat():
    num_users = len(username_password.keys())
    num_tasks = len(task_list)

    print("-----------------------------------")
    print(f"Number of users: \t\t {num_users}")
    print(f"Number of tasks: \t\t {num_tasks}")
    print("-----------------------------------")

def disp_report():
    usr_name = []
    per_nm = 0
    tsk_cmpl = 0
    tsk_ovrdure = 0
    total_task_comp = 0
    total_task_ovr = 0
    total_nm_tasks = len(task_list)
    for usrs in user_data:   # find how many uses we have
        u = usrs.split(";")
        usr_name.append(u[0])
    str_users_overview = f"Total number of users: {len(usr_name)}\n"
    str_users_overview += f"Total number of tasks: {total_nm_tasks}\n"
    str_tasks_overview = f"Total number of tasks: {total_nm_tasks}\n"
    #print(str_overview)
    for usr in range(0, len(usr_name)):
        tsk_ovrdure = 0
        # Calculate the percentage of tasks assigned to each used
        per_nm = round(int(sel_usr(usr_name[usr], 0)) / int(total_nm_tasks) * 100)
        str_users_overview += f"To user {(usr_name[usr]).capitalize()} has been assigned {per_nm} % of tasks\n"
        # Calculate the percentage of tasks completed by users and the tasks that are overdue
        for t in task_list:
            if t['username'] == usr_name[usr]:
                if t['completed']:
                    tsk_cmpl += 1
                elif (t['completed'] == False) and (str(date.today()) > str(t['due_date'].strftime(DATETIME_STRING_FORMAT))):
                    tsk_ovrdure += 1
        if(tsk_cmpl!=0):
            per_nm = round(int(tsk_cmpl) / int(sel_usr(usr_name[usr], 0)) * 100)
            str_users_overview += f"{(usr_name[usr]).capitalize()} has completed {per_nm}%\n"
            str_users_overview += f"{(usr_name[usr]).capitalize()} has uncompleted {100 - per_nm}%\n"
            per_nm = round(int(tsk_ovrdure) / int(sel_usr(usr_name[usr], 0)) * 100)
            str_users_overview += f"{(usr_name[usr]).capitalize()} has been overdue {per_nm}% of tasks\n"
        else:
            per_nm = 0
            str_users_overview += f"{(usr_name[usr]).capitalize()} has completed {per_nm}%\n"
            str_users_overview += f"{(usr_name[usr]).capitalize()} has uncompleted {100 - per_nm}%\n"
            if(tsk_ovrdure != 0):
                per_nm = round(int(tsk_ovrdure) / int(sel_usr(usr_name[usr], 0)) * 100)
                str_users_overview += f"{(usr_name[usr]).capitalize()} has been overdue {per_nm}% of tasks\n"
        total_task_comp += tsk_cmpl
        total_task_ovr += tsk_ovrdure
    str_tasks_overview += f"Total completed tasks: {total_task_comp}\n"
    str_tasks_overview += f"Total number uncompleted tasks: {total_nm_tasks - total_task_comp}\n"
    str_tasks_overview += f"Total number overdue tasks: {total_task_ovr}\n"
    str_tasks_overview += f"Total percentage of uncompleted tasks: " \
                          f"{round((total_nm_tasks - total_task_comp)/total_nm_tasks*100)}%\n"
    str_tasks_overview += f"Total percentage of overdue tasks: " \
                          f"{round((total_task_ovr) / total_nm_tasks * 100)}%\n"
    print(str_users_overview)
    with open('user_overview.txt', 'w') as f_usr:
        f_usr.write(str_users_overview)
    with open('task_overview.txt', 'w') as f_tsk:
        f_tsk.write(str_tasks_overview)
    print(str_tasks_overview)

def sel_usr(user,completed):
    u_nm = 0
    for t in task_list:
        if t['username']==user:
            u_nm += 1
    return u_nm

# print input menu to display after login
def print_input_menu(curr_user):
    if curr_user == "admin":
        insert_ds = "\n\tgr - Generate reports"
    else:
        insert_ds = ""
    text = (f'''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task 
    ds - Display statistics {insert_ds}
    "e - Exit"
    : ''')
    return text

def save_data(task_nm, user, date, complete):  #modify this
    new_data = task_data[int(task_nm)-1].split(";")
    if user != "0":
        new_data[0] = user
        task_data[int(task_nm)-1] = ";".join(new_data)
        sv_data = "\n".join(task_data)
        with open('tasks.txt', 'w') as f:
            f.write(sv_data)
    elif date != "0":
        new_data[3] = date
        task_data[int(task_nm) - 1] = ";".join(new_data)
        sv_data = "\n".join(task_data)
        with open('tasks.txt', 'w') as f:
            f.write(sv_data)
    elif complete != "0":
        new_data[5] = complete
        task_data[int(task_nm) - 1] = ";".join(new_data)
        sv_data = "\n".join(task_data)
        with open('tasks.txt', 'w') as f:
            f.write(sv_data)

def pr_menu(sl_opt1, sl_opt2, sl_opt3, sl_opt4):
    print("-"*20 + "Edit Option" + "-"*20)
    print(f"1 - {sl_opt1}\t 2 - {sl_opt2}\t 3 - {sl_opt3}\t 4 - {sl_opt4}")
    print("-" * 51)

