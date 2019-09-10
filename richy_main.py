#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Richy.
Personal assistant made especially for GNU/Linux because we deserve our own version of Siri too!

Usage:
 richy
 richy [your question here]

Options:
  -h, --help  displays help
"""
from __future__ import print_function

# --------------------------------  Startup  -----------------------------------

""" Modules to import """
from colorama import init, Fore
import os
import sys
import json
import time
import random
import httplib2
import wikipedia
from guessit import *
from time import sleep
from timeit import timeit
from bs4 import BeautifulSoup
from os.path import expanduser
import xml.etree.ElementTree as ET



""" Set up python 2.7 functions to work on python 3.4, 3.5 """
try:
    input = raw_input
    range = xrange
    from urllib import urlopen, urlencode
except NameError:
    from urllib.request import urlopen
    from urllib.parse import urlencode



""" Setting variables """
current_path = os.path.dirname(os.path.abspath(__file__))
config_path = expanduser("~/.richy/config/")
modules_path = expanduser("~/.richy/modules/")
clear = lambda: os.system('clear')
sys.dont_write_bytecode = True
schedule_list_for_today = [];



""" Checking for first setup """
config_file = ".richy/config/config.conf"
is_config_file = os.path.isfile(config_file)


if is_config_file:
    import configparser
    config = configparser.ConfigParser()
    config.read(config_file)
    first_time = config.get('main_settings', 'first_time')

    """ First time setup """
    if first_time == "True":
        first_setup = modules_path + "first_setup.py"
        sys.path.append(modules_path)
        import first_setup
        first_setup.firstTime()


elif not is_config_file:

    print(Fore.BLUE + "Richy: " + Fore.RED + "It seems like Richy wasn't able to detect config file which is required to run it." + Fore.WHITE)
    print(Fore.BLUE + "Richy: " + Fore.RED + "Please redownload Richy with rest of the files..." + Fore.WHITE)
    print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting..." + Fore.WHITE)
    sys.exit()



""" Checking for config file & importing it """
config_file = config_path + "config.conf"
is_config_file = os.path.isfile(config_file)

if is_config_file:

    """ Importing config"""
    import configparser
    config = configparser.ConfigParser()
    config.read(config_file)

    """ Loading user info """
    name = config.get('user_info', 'name')
    date_of_birth = config.get('user_info', 'date_of_birth')

    """ Loading main settings """
    first_time = config.get('main_settings', 'first_time')
    show_version = config.get('main_settings', 'show_version')
    coloured_version = config.get('main_settings', 'coloured_version')
    clear_commands = config.get('main_settings', 'clear_commands')
    additional_search = config.get('main_settings', 'additional_search')
    letter_color = config.get('main_settings', 'letter_color')
    terminal_columns = config.get('main_settings', 'terminal_columns')
    terminal_rows = config.get('main_settings', 'terminal_rows')

    """ Loading schedule module settings """
    schedule_module = config.get('schedule_module', 'schedule_module')
    schedule_date_format = config.get('schedule_module', 'schedule_date_format')

    """ Loading multimedia module settings """
    multimedia_module = config.get('multimedia_module', 'multimedia_module')
    movie_directory = config.get('multimedia_module', 'movie_directory')


    try:
        terminal_columns = int(terminal_columns)
        terminal_rows = int(terminal_rows)
    except:
        print(Fore.BLUE + "Richy: " + Fore.RED + "Values for terminal size are incorrect, please change them in config and restart Richy." + Fore.WHITE)
        print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting..." + Fore.WHITE)
        sys.exit()

elif not is_config_file:

    print(Fore.BLUE + "Richy: " + Fore.RED + "It seems like Richy wasn't able to detect config file which is required to run it." + Fore.WHITE)
    print(Fore.BLUE + "Richy: " + Fore.RED + "Please redownload Richy with rest of the files..." + Fore.WHITE)
    print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting..." + Fore.WHITE)
    sys.exit()



""" Checking for data file & opening it """
data_file = config_path + "/data.json"
is_data_file = os.path.isfile(data_file)

if is_data_file:

    """ Loading data file into memory """
    with open(data_file, "r+") as data_file_open:
        data = json.load(data_file_open)

elif not is_data_file:

    print(Fore.BLUE + "Richy: " + Fore.RED + "It seems like Richy wasn't able to detect data file which is required to run it." + Fore.WHITE)
    print(Fore.BLUE + "Richy: " + Fore.RED + "Please redownload Richy with rest of the files..." + Fore.WHITE)
    print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting..." + Fore.WHITE)
    sys.exit()



""" Checking for logo_printer script & opening it """
logo_printer_script = modules_path + "logo_printer.py"
is_logo_printer_script = os.path.isfile(logo_printer_script)

if is_logo_printer_script:

    sys.path.append(modules_path)
    import logo_printer

elif not is_logo_printer_script:

    print(Fore.BLUE + "Richy: " + Fore.RED + "It seems like Richy wasn't able to detect logo printer script which is required to run it." + Fore.WHITE)
    print(Fore.BLUE + "Richy: " + Fore.RED + "Please redownload Richy with rest of the files..." + Fore.WHITE)
    print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting..." + Fore.WHITE)
    sys.exit()


""" Checking for schedule module, schedule file & loading them into memory """
if schedule_module == "On":

    """ Loading schedule module & schedule file """
    schedule_file = config_path + "schedule.json"
    schedule_module_file = modules_path + "schedule.py"
    is_schedule_file = os.path.isfile(schedule_file)
    is_schedule_module = os.path.isfile(schedule_module_file)

    if is_schedule_file and is_schedule_module:

        with open(schedule_file, "r+") as schedule_file_open:
            schedule = json.load(schedule_file_open)

    elif not is_schedule_file or not is_schedule_module:

        print(Fore.BLUE + "Richy: " + Fore.RED + "It seems like Richy wasn't able to detect schedule module or schedule file which is required to run schedule module." + Fore.WHITE)
        print(Fore.BLUE + "Richy: " + Fore.RED + "Please redownload Richy with rest of the files or turn off schedule module in config." + Fore.WHITE)
        print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting..." + Fore.WHITE)
        sys.exit()

elif not schedule_module == "On" or not schedule_module == "Off":

    print(Fore.BLUE + "Richy: " + Fore.RED + "schedule_module value is invalid. Please change it in config to either On or Off." + Fore.WHITE)
    print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting..." + Fore.WHITE)
    sys.exit()



""" Loading multimedia module & loading it into memory """
if multimedia_module == "On":

    multimedia_module_file = modules_path + "multimedia.py"
    is_multimedia_module = os.path.isfile(multimedia_module_file)

    if is_multimedia_module:

        sys.path.append(modules_path)
        import multimedia

    elif not is_multimedia_module:

        print(Fore.BLUE + "Richy: " + Fore.RED + "It seems like Richy wasn't able to detect multimedia module file which is required to run multimedia module." + Fore.WHITE)
        print(Fore.BLUE + "Richy: " + Fore.RED + "Please redownload Richy with rest of the files or turn off multimedia module in config." + Fore.WHITE)
        print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting..." + Fore.WHITE)
        sys.exit()

elif not multimedia_module == "On" or not multimedia_module == "Off":

    print(Fore.BLUE + "Richy: " + Fore.RED + "multimedia_module value is invalid. Please change it in config to either On or Off." + Fore.WHITE)
    print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting..." + Fore.WHITE)
    sys.exit()



""" Setting up format of the dates """
if schedule_date_format.lower() == "dd/mm/yyyy":
    schedule_date_format_type = 1
    todays_date = str(time.strftime("%d/%m/%Y"))
elif schedule_date_format.lower() == "mm/dd/yyyy":
    schedule_date_format_type = 2
    todays_date = str(time.strftime("%m/%d/%Y"))
elif schedule_date_format.lower() == "yyyy/mm/dd":
    schedule_date_format_type = 3
    todays_date = str(time.strftime("%Y/%m/%d"))
elif schedule_date_format.lower() == "yyyy/dd/mm":
    schedule_date_format_type = 4
    todays_date = str(time.strftime("%Y/%d/%m"))
else:
    print(Fore.BLUE + "Richy: " + Fore.RED + "Invalid date format, please change 'schedule_date_format' in config file  to suitable format.")
    print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting...")
    sys.exit()
todays_date = str(time.strftime("%d/%m/%Y"))




# --------------------------------  Functions  ---------------------------------

def list_schedule():
    """ List the schedule """
    total_task_number_today = 0
    print("Your today's schedule;")
    with open(schedule_file, "r+") as schedule_file_open:
        schedule = json.load(schedule_file_open)
        for task in schedule["schedule_list"].keys():
            if schedule["schedule_list"][task] == todays_date:
                print("- " + task)
                total_task_number_today = total_task_number_today + 1
    if total_task_number_today == 0:
        print("- Your schedule is empty for today!")
    print("\n")

def print_main_screen():
    """ Print main 'Richy' text & logo """
    if terminal_columns <= 55:
        logo_printer.small(show_version, coloured_version, letter_color)
    elif terminal_columns >= 56 and terminal_columns <= 70:
        logo_printer.small_medium(show_version, coloured_version, letter_color)
    elif terminal_columns > 70 and terminal_columns <= 100:
        logo_printer.medium(show_version, coloured_version, letter_color)
    elif terminal_columns >= 100:
        logo_printer.large(show_version, coloured_version, letter_color)


def print_schedule():
    """ Check if schedule module is on then print it """
    print("\n")
    if schedule_module == "On":
        list_schedule()
    elif schedule_module == "Off":
        print("\n")

def check_birthday():
    """ Check if its users' birthday """
    if schedule_date_format_type == 1:
        if date_of_birth[:5] == str(time.strftime("%d/%m")):
            print(Fore.YELLOW + "Happy Birthday, " + name + "!\n" + Fore.WHITE)
    elif schedule_date_format_type == 2:
        if date_of_birth[:5] == str(time.strftime("%m/%d")):
            print(Fore.YELLOW + "Happy Birthday, " + name + "!\n" + Fore.WHITE)
    elif schedule_date_format_type == 3:
        if date_of_birth[5:10] == str(time.strftime("%m/%d")):
            print(Fore.YELLOW + "Happy Birthday, " + name + "!\n" + Fore.WHITE)
    elif schedule_date_format_type == 4:
        if date_of_birth[5:10] == str(time.strftime("%d/%m")):
            print(Fore.YELLOW + "Happy Birthday, " + name + "!\n" + Fore.WHITE)

def response(query):
    """ Gets answer for users' query from wolframalpha servers """
    query = query.lower()
    query_original = query
    query = urlencode({'input':query})
    app_id = "Q6254U-URKKHH9JLL"
    wolfram_api = "http://api.wolframalpha.com/v2/query?appid="+app_id+"&format=plaintext&podtitle=Result&"+query
    resp, content = httplib2.Http().request(wolfram_api)
    root = ET.fromstring(content)
    error = root.get('error')
    success = root.get('success')
    numpods = root.get('numpods')
    answer= ''
    if success and int(numpods) > 0 :
        for plaintext in root.iter('plaintext'):
            if isinstance(plaintext.text, str) :
                answer = answer + plaintext.text
        return answer
    elif error:
        me_no_english1 = "Sorry, I didn't understood that."
        me_no_english2 = "I didn't get that."
        me_no_english3 = "I can't understand what you said."
        me_no_english4 = "It seems like I can't answer this question."
        me_no_english = [me_no_english1, me_no_english2, me_no_english3, me_no_english4]

        if additional_search == "True":
            query_original = query_original.replace(" ", "_")
            r = urlopen("https://www.evi.com/q/" + query_original).read()
            whole_content = BeautifulSoup(r, "lxml")
            answer = str(whole_content.find(class_="tk_common"))
            length = int(len(str(answer)))
            first_length = length - 9
            answer = answer[25:first_length]
            if answer.find('None'):
                return random.choice(me_no_english)
            else:
                return answer

        elif additional_search == "False":
            return random.choice(me_no_english)

        elif additional_search == "Ask":
            print("It seems like I can't answer this question.")
            print("Do you want me to send query to Evi? [Y/N]")
            user_input = input("[Y/N] >")
            if user_input == "Y" or user_input == "y":
                query_original = query_original.replace(" ", "_")
                r = urlopen("https://www.evi.com/q/" + query_original).read()
                whole_content = BeautifulSoup(r, "lxml")
                answer = str(whole_content.find(class_="tk_common"))
                length = int(len(str(answer)))
                first_length = length - 9
                answer = answer[25:first_length]
                if answer.find('None'):
                    return random.choice(me_no_english)
                else:
                    return answer
            elif user_input == "N" or user_input == "n":
                return "\n"
            else:
                return "Wrong command."

def user_input_search(user_input):
    """ Checks user input in data.json, if not it sends request to wolframalpha """
    local = 0
    user_input = user_input.lower()
    for item in data["data-response"]:
        if item == user_input or item == user_input[:10] or item == user_input[:11] or item == user_input[:12] or item == user_input[:13] or item == user_input[:5]:
            if data["data-response"][item] == "1":
                local = 1
                try:
                    exec(compile(open(schedule_module_file).read(), schedule_module_file, 'exec'))
                except:
                   print("There's been error with loading schedule module. Are you sure schedule module has been turned on?")
                pause = input()
                break

            elif data["data-response"][item] == "2":
                local = 1
                try:
                    multimedia.index_all()
                except:
                    print("There's been error with loading multimedia module. Are you sure multimedia module has been turned on? If the error will persist, please try running 'richy' and then your command. If this also didn't help, try running richy from the script and then your command.")
                pause = input()
                break

            elif data["data-response"][item] == "3":
                local = 1
                try:
                    if user_input.find("--") == -1:
                        args = "none"
                        multimedia.list_all(args)
                    else:
                        args = "--" + user_input.split('--', 1)[1]
                        multimedia.list_all(args)
                except:
                    print("There's been error with loading multimedia module. Are you sure multimedia module has been turned on? If the error will persist, please try running 'richy' and then your command. If this also didn't help, try running richy from the script and then your command.")
                pause = input()
                break

            elif data["data-response"][item] == "4":
                local = 1
                try:
                    multimedia.movies_help()
                except:
                    print("There's been error with loading multimedia module. Are you sure multimedia module has been turned on? If the error will persist, please try running 'richy' and then your command. If this also didn't help, try running richy from the script and then your command.")
                pause = input()
                break

            elif data["data-response"][item] == "5":
                local = 1
                try:
                    users_movie_name = user_input[13:]
                    multimedia.single_movie_info(users_movie_name)
                except:
                    print("There's been error with loading multimedia module. Are you sure multimedia module has been turned on? If the error will persist, please try running 'richy' and then your command. If this also didn't help, try running richy from the script and then your command.")
                pause = input()
                break
            elif data["data-response"][item] == "6":
                local = 1
                if user_input[:10] == "wikipedia ":
                    search_term = user_input[10:]
                else:
                    search_term = user_input[5:]
                list_of_associated_articles = wikipedia.search(search_term)
                try:
                    wanted_article = list_of_associated_articles[0]
                    print(wikipedia.summary(wanted_article))
                except:
                    print("\nRichy was unable to find an article which is associated with your search term.")
                pause = input()

    if local == 0:
        print(response(user_input))
        pause = input()

def terminal_size():
    """ Changing the size of the terminal """
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=terminal_rows, cols=terminal_columns))

def start_up():
    sleep(1)
    clear()

    terminal_size()

    if clear_commands == "True":
        while True:

            """ Printing main 'Richy' text """
            clear()
            print_main_screen()

            """ Printing out schedule """
            print_schedule()

            """ Printing out 'happy birthday' """
            check_birthday()

            """ Asking for user input """
            print("How can I help you today, " + name + "?")
            user_input = input(">")

            """ Searching for answer """
            user_input_search(user_input)



    elif clear_commands == "False":

        """ Printing main 'Richy' text """
        print_main_screen()

        """ Printing out schedule """
        print_schedule()

        """ Printing out 'happy birthday' """
        check_birthday()

        while True:

            """ Asking for user input """
            print("How can I help you today, " + name + "?")
            user_input = input(">")

            """ Searching for answer """
            user_input_search(user_input)

    else:
        print(Fore.BLUE + "Richy: " + Fore.RED + "Variable clear_commands has invalid value, please change it in config file to either True or False." + Fore.WHITE)
        print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting..." + Fore.WHITE)
        sys.exit()

def main():
    """ Gets arguments from terminal and passes them further """
    arguments = ""
    if len(sys.argv) == 1:
        start_up()
    else:
        for argument in sys.argv:
            if not argument == sys.argv[0]:
                if argument == sys.argv[1]:
                    arguments = arguments + argument
                    first_argument = 0
                elif not argument == sys.argv[1]:
                    arguments = arguments + " " + argument
    user_input_search(arguments)



# -----------------------------------  Main  -----------------------------------


if __name__ == '__main__':
    main()
