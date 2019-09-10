#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os


def firstTime():

    """ Set up python 2.7 functions to work on python 3.4, 3.5 """
    try:
        input = raw_input
        range = xrange
        from urllib import urlopen, urlencode
    except NameError:
        from urllib.request import urlopen
        from urllib.parse import urlencode
    clear = lambda: os.system('clear')
    config_path = os.path.expanduser("~/.richy/config")
    config_file = config_path + "/config.conf"
    from builtins import input


    # -----------------------------------  Main  -----------------------------------
    """ Importing config"""
    import configparser
    config = configparser.ConfigParser()
    config.read(config_file)
    config.set('main_settings', 'first_time', "False")



    clear()
    print("                     ooooooooo.    o8o            oooo                     ")
    print("                     `888   `Y88.  `''            `888                     ")
    print("                      888   .d88' oooo   .ooooo.   888 .oo.   oooo    ooo  ")
    print("                      888ooo88P'  `888  d88' `'Y8  888P'Y88b   `88.  .8'   ")
    print("                      888`88b.     888  888        888   888    `88..8'    ")
    print("                      888  `88b.   888  888   .o8  888   888     `888'     ")
    print("                     o888o  o888o o888o `Y8bod8P' o888o o888o     .8'      ")
    print("                                                               .o..P'     0.50_Beta  ")
    print("\n")

    print("Welcome to Richy, your personal assistant.",
    "\nAs this is the first time you are running Richy, do you want to go over some settings?")
    answer = input("[y/n] >")
    if answer == "n":
        print("\nIf you change your mind, you can always change them in ~/.richy/config/config.conf.")
        input()
    elif answer == "y":

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
        colored_version = config.get('main_settings', 'coloured_version')
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


        print("\n")
        print("Okay, let's start with a simple one, how do you want Richy to call you?")
        name = input(">")
        config.set('user_info', 'name', name)

        print("\n")
        print("Your date of birth in dd/mm/yyyy format (only used for 'Happy Birthday' message):")
        date_of_birth = input(">")
        config.set('user_info', 'date_of_birth', date_of_birth)

        config.set('main_settings', 'first_time', "0")

        print("\n")
        print("Do you want Richy to show its version on the main screen? [y/n]")
        show_version = input(">")
        if show_version == "y":
            show_version = "True"
            config.set('main_settings', 'show_version', show_version)
        elif show_version == "n":
            show_version = "False"
            config.set('main_settings', 'show_version', show_version)
        else:
            print("Invalid value, exiting...")
            sys.exit()

        print("\n")
        print("Do you want the version to be the same colour as the main 'Richy' text? [y/n]")
        colored_version = input(">")
        if colored_version == "y":
            colored_version = "True"
            config.set('main_settings', 'colored_version', colored_version)
        elif colored_version == "n":
            colored_version = "False"
            config.set('main_settings', 'colored_version', colored_version)
        else:
            print("Invalid value, exiting...")
            sys.exit()

        print("\n")
        print("Do you want Richy to go back to main screen and clear previous answer every time you hit enter? [y/n]")
        clear_commands = input(">")
        if clear_commands == "y":
            clear_commands = "True"
            config.set('main_settings', 'clear_commands', clear_commands)
        elif clear_commands == "n":
            clear_commands = "False"
            config.set('main_settings', 'clear_commands', clear_commands)
        else:
            print("Invalid value, exiting...")
            sys.exit()

        print("\n")
        print("If Richy won't be able to find answer to your query on wolframalpha servers, do you want Richy to ask Evi? (www.evi.com)? [y/n]")
        additional_search = input(">")
        if additional_search == "y":
            additional_search = "True"
            config.set('main_settings', 'additional_search', additional_search)
        elif additional_search== "n":
            additional_search = "False"
            config.set('main_settings', 'additional_search', additional_search)
        else:
            print("Invalid value, exiting...")
            sys.exit()

        print("\n")
        print("What colour do you want Richy's letters to be? [BLUE, GREY, PINK, YELLOW, GREEN, RED, WHITE]")
        letter_color = input(">")
        if letter_color == "BLUE" or letter_color == "Blue" or letter_color == "blue":
            letter_color = "BLUE"
            config.set('main_settings', 'letter_color', letter_color)
        elif letter_color == "GREY" or letter_color == "Grey" or letter_color == "grey":
            letter_color = "GREY"
            config.set('main_settings', 'letter_color', letter_color)
        elif letter_color == "PINK" or letter_color == "Pink" or letter_color == "pink":
            letter_color = "PINK"
            config.set('main_settings', 'letter_color', letter_color)
        elif letter_color == "YELLOW" or letter_color == "Yellow" or letter_color == "yellow":
            letter_color = "YELLOW"
            config.set('main_settings', 'letter_color', letter_color)
        elif letter_color == "GREEN" or letter_color == "Green" or letter_color == "green":
            letter_color = "GREEN"
            config.set('main_settings', 'letter_color', letter_color)
        elif letter_color == "RED" or letter_color == "Red" or letter_color == "red":
            letter_color = "RED"
            config.set('main_settings', 'letter_color', letter_color)
        elif letter_color == "WHITE" or letter_color == "White" or letter_color == "white":
            letter_color = "WHITE"
            config.set('main_settings', 'letter_color', letter_color)
        else:
            print("Invalid value, exiting...")
            sys.exit()

        print("\n")
        print("How many columns (size) do you want your terminal to be when you run Richy? (Recommend is 125)")
        terminal_columns = input(">")
        if terminal_columns.isdigit() == True:
            config.set('main_settings', 'terminal_columns', terminal_columns)
        else:
            print("Invalid value, exiting...")
            sys.exit()

        print("\n")
        print("How many rows (size) do you want your terminal to be when you run Richy? (Recommend is 30)")
        terminal_rows = input(">")
        if terminal_rows.isdigit() == True:
            config.set('main_settings', 'terminal_rows', terminal_rows)
        else:
            print("Invalid value, exiting...")
            sys.exit()

        print("\n")
        print("Whats your prefered date format? (recommended is dd/mm/yyyy)")
        schedule_date_format = input(">")
        config.set('schedule_module', 'schedule_date_format', schedule_date_format)

        print("\n")
        print("Whats the path to the folder with movies?")
        movie_directory = input(">")
        config.set('multimedia_module', 'movie_directory', movie_directory)

        with open(config_file, 'w') as config_file_open:
            config.write(config_file_open)

        print("\n")
        print("Thanks for setting up Richy, now Richy should start after pressing enter.")
        input()

    else:
        print("Invalid answer, exiting...")
        sys.exit()
