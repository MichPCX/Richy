# -*- coding: UTF-8 -*-

# Richy module info
# [Name] = schedule
# [Description] = schedule module allows to modify your schedule which then will be displayed in Richy
# [Latest update in] = 0.38_Alpha



# --------------------------------  Startup  -----------------------------------
""" Importing main modules """
from __future__ import print_function
import os
import sys
import time
import json
import calendar
from colorama import *
from unipath import Path
from json import JSONEncoder
from json import JSONDecoder
from sys import platform as _platform



""" Setting variables """
current_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.expanduser("~/.richy/config")
modules_path = os.path.expanduser("~/.richy/modules")

config_file = config_path + "/config.conf"
schedule_file = config_path + "/schedule.json"



""" Opening the schedule file, importing settings from config file and setting variables """
with open(schedule_file, "r+") as schedule_file_open:
    schedule = json.load(schedule_file_open)

import configparser
config = configparser.ConfigParser()
config.read(config_file)
schedule_date_format = config.get('schedule_module', 'schedule_date_format')
todays_date = str(time.strftime("%d/%m/%Y"))
exit_code = 0



""" Making it 2.7 & 3.5 compatible """
try:
    # Python2
    input = raw_input
    range = xrange
except NameError:
    # Python3
    pass



""" Colorama """
init()



""" Setting up format of the dates """
if schedule_date_format == "DD/MM/YYYY":
    schedule_date_format_type = 1
    formatted_date = todays_date
elif schedule_date_format == "MM/DD/YYYY":
    schedule_date_format_type = 2
    formatted_date = todays_date[3:5] + "/" + todays_date[0:2] + "/" + todays_date[6:10]
elif schedule_date_format == "YYYY/MM/DD":
    schedule_date_format_type = 3
    formatted_date = todays_date[6:10] + "/" + todays_date[3:5] + "/" + todays_date[0:2]
elif schedule_date_format == "YYYY/DD/MM":
    schedule_date_format_type = 4
    formatted_date = todays_date[6:10] + "/" + todays_date[0:2] + "/" + todays_date[3:5]
else:
    print("Invalid date format, please change 'schedule_date_format' in config file...")
    print("Exiting...")
    sys.exit()



# --------------------------------  Functions  ---------------------------------
def list_schedule_full():
    """ Listing all the tasks in the schedule """
    print("\n")
    with open(schedule_file, "r+") as schedule_file_open:
        schedule = json.load(schedule_file_open)
        total_task_number = 0
        for each_task in schedule["schedule_list"].keys():
            date = schedule["schedule_list"][each_task]
            if schedule_date_format_type == 1:
                formatted_date = date
            elif schedule_date_format_type == 2:
                formatted_date = date[3:5] + "/" + date[0:2] + "/" + date[6:10]
            elif schedule_date_format_type == 3:
                formatted_date = date[6:10] + "/" + date[3:5] + "/" + date[0:2]
            elif schedule_date_format_type == 4:
                formatted_date = date[6:10] + "/" + date[0:2] + "/" + date[3:5]
            print("- " + each_task + " (" + formatted_date + ")")
            total_task_number = total_task_number + 1
    if total_task_number == 0:
        print("- Your schedule is empty!")

# -----------------------------------  Main  -----------------------------------

print("\n")
print("Welcome to schedule module of Richy. Here you can manage your schedule. Use 'help' if you need help.")

while exit_code == 0:
    print("Your full schedule including dates;")
    list_schedule_full()

    """ User input """
    user_input = input("schedule>")
    user_input = user_input.lower()

    """ Commands """

    """ Help - displays help """
    if user_input == "help" or user_input == "--help" or user_input == "help me" or user_input == "i need help":
        print("\n")
        print("Welcome to schedule module where you can modify your daily schedule. You can add/remove/change events how ever",
        "you want. Just use one of the commands below;")
        print("\n")
        print(Fore.BLUE + "add " + Fore.GREEN + "[name of the task]" + Fore.WHITE + " - adds new task to the schedule,")
        print(Fore.BLUE + "remove " + Fore.GREEN + "[name of the task]" + Fore.WHITE + " - removes the task from the schedule,")
        print(Fore.BLUE + "rename " + Fore.GREEN + "[name of the task]" + Fore.WHITE + " - changes the name of already existing task,")
        print(Fore.BLUE + "move " + Fore.GREEN + "[name of the task]" + Fore.WHITE + " - moves one task to another date")
        print(Fore.BLUE + "exit" + Fore.WHITE + " - exits schedule module")

    """ Add - add the task to schedule """
    elif user_input[:4] == "add ":
        task = user_input.split(' ', 1)[1]
        print(" Adding '" + task + "' to the schedule list, please type in a date for this task in the format " + schedule_date_format)
        year = int(time.strftime("%Y"))
        month = int(time.strftime("%m"))
        cal = calendar.month(year, month)

        if schedule_date_format_type == 1:
            formatted_date = todays_date
        elif schedule_date_format_type == 2:
            formatted_date = todays_date[3:5] + "/" + todays_date[0:2] + "/" + todays_date[6:10]
        elif schedule_date_format_type == 3:
            formatted_date = todays_date[6:10] + "/" + todays_date[3:5] + "/" + todays_date[0:2]
        elif schedule_date_format_type == 4:
            formatted_date = todays_date[6:10] + "/" + todays_date[0:2] + "/" + todays_date[3:5]

        print("\n" + cal + "Todays date is: " + formatted_date)
        date_of_task = input("schedule, date>")
        if date_of_task == "":
            print("You haven't chosen any date, selecting todays date...")
            schedule["schedule_list"][task] = formatted_date
            with open(schedule_file, 'w') as schedule_file_open:
                json.dump(schedule, schedule_file_open)
            print("Your task has been added.")
            print("\n")
        elif date_of_task[:2].isdigit() == False:
            print("This is not a date!")
            print("\n")
        else:
            schedule["schedule_list"][task] = date_of_task
            with open(schedule_file, 'w') as schedule_file_open:
                json.dump(schedule, schedule_file_open)
            print("Your task has been added.")
            print("\n")

    """ Remove - deletes the task from the schedule """
    elif user_input[:7] == "remove " or user_input[:7] == "delete ":
        task = user_input.split(' ', 1)[1]
        if task in list(schedule["schedule_list"].keys()):
            del schedule["schedule_list"][task]
            print("Your task has been deleted.")
            print("\n")
            with open(schedule_file, 'w') as schedule_file_open:
                json.dump(schedule, schedule_file_open)
        else:
            print("That task is not on the list!")
            print("\n")


    """ Rename - rename the task """
    elif user_input[:7] == "rename " or user_input[:12] == "change name ":
        task = user_input.split(' ', 1)[1]
        if task in list(schedule["schedule_list"].keys()):
            date = schedule["schedule_list"][task]
            print("Type in new name for this task;")
            new_task_name = input("schedule, new_task_name>")
            del schedule["schedule_list"][task]
            schedule["schedule_list"][new_task_name] = date
            with open(schedule_file, 'w') as schedule_file_open:
                json.dump(schedule, schedule_file_open)
            print("Your task's name has been changed.")
            print("\n")
        elif task not in list(schedule["schedule_list"].keys()):
            print("That task is not on the list!")
            print("\n")

    """ Move - moves the task to different date """
    elif user_input[:5] == "move ":
        task = user_input.split(' ', 1)[1]
        if task in list(schedule["schedule_list"].keys()):
            print("Type in new date for this task;")
            year = int(time.strftime("%Y"))
            month = int(time.strftime("%m"))
            cal = calendar.month(year, month)
            print("\n" + cal + "Todays date is: " + formatted_date)
            new_task_date = input("schedule, new_task_date " + schedule_date_format + ">")
            if new_task_date[:2].isdigit() == True:
                if schedule_date_format_type == 2:
                    new_task_date = new_task_date[3:5] + "/" + new_task_date[0:2] + "/" + new_task_date[6:10]
                elif schedule_date_format_type == 3:
                    new_task_date = new_task_date[8:10] + "/" + new_task_date[5:7] + "/" + new_task_date[0:4]
                elif schedule_date_format_type == 4:
                    new_task_date = new_task_date[5:7] + "/" + new_task_date[8:10] + "/" + new_task_date[0:4]
                del schedule["schedule_list"][task]
                schedule["schedule_list"][task] = new_task_date
                with open(schedule_file, 'w') as schedule_file_open:
                    json.dump(schedule, schedule_file_open)
                print("Your task has been moved.")
                print("\n")
            else:
                print("This date is invalid.")
                print("\n")
        elif task not in list(schedule.keys()):
            print("That task is not on the list!")
            print("\n")

    """ Exit - exits the module to go back to Richy """
    elif user_input == "exit":
        print("You are about to exit 'schedule module'. Are you sure you want to continue? [Y/N]")
        user_input = input("schedule, [Y/N]>")
        if user_input.lower() == "y":
            exit_code = 1
        elif user_input.lower() == "n":
            print("Alright then, you can carry on to modify your schedule.")
            print("\n")
        else:
            print("Invalid command.")
            print("\n")

    """ Invalid command """
    else:
        print("Invalid command.")
        print("\n")
