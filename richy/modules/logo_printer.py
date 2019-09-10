#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from colorama import init, Fore, Style
import sys
init()



""" Set up python 2.7 functions to work on python 3.4, 3.5 """
try:
    input = raw_input
    range = xrange
    from urllib import urlopen, urlencode
except NameError:
    from urllib.request import urlopen
    from urllib.parse import urlencode



# --------------------------------  Functions  ---------------------------------

def small(show_version, coloured_version, letter_color):

    """ Setting up the colour of the letters and printing the text in it """
    init()
    if letter_color == "BLUE" or letter_color == "Blue" or letter_color == "blue":
        color_changer = Fore.BLUE
    elif letter_color == "GREY" or letter_color == "Grey" or letter_color == "grey":
        color_changer = Fore.GREY
    elif letter_color == "PINK" or letter_color == "Pink" or letter_color == "pink":
        color_changer = Fore.PINK
    elif letter_color == "YELLOW" or letter_color == "Yellow" or letter_color == "yellow":
        color_changer = Fore.YELLOW
    elif letter_color == "GREEN" or letter_color == "Green" or letter_color == "green":
        color_changer = Fore.GREEN
    elif letter_color == "RED" or letter_color == "Red" or letter_color == "red":
        color_changer = Fore.RED
    elif letter_color == "WHITE" or letter_color == "White" or letter_color == "white":
        color_changer = Fore.WHITE
    else:
        print(Fore.BLUE + "Richy: " + Fore.RED + "Invalid letter_color value. Please change it in config and restart Richy.")
        print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting...")
        sys.exit()

    if show_version == "True":
        if coloured_version == "True":
            print(color_changer + "                      Richy       " + Fore.RESET)
            print(color_changer + "                         0.50_Beta    " + Fore.RESET)
        elif coloured_version == "False":
            print(color_changer + "                      Richy       " + Fore.RESET)
            print("                         0.50_Beta    ")
        else:
            print(Fore.BLUE + "Richy: " + Fore.RED + "Invalid coloured_version value. Please change it to True or False in config.")
            print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting...")
            sys.exit()
    elif show_version == "False":
        print(color_changer + "                      Richy       " + Fore.RESET)
    else:
        print(Fore.BLUE + "Richy: " + Fore.RED + "Invalid show_version value. Please change it to True or False in config.")
        print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting...")
        sys.exit()


def small_medium(show_version):
    print(Fore.BLUE + "                      $$$$$$$$$$$$$$$$$$$$" + Fore.RESET)
    print(Fore.BLUE + "                 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$" + Fore.RESET)
    print(Fore.BLUE + "              $$$$$$$" + Fore.CYAN + "IIIIIIIIIIIIIIIIIIII7" + Fore.BLUE + "$$$$$$" + Fore.RESET)
    print(Fore.BLUE + "            $$$$$$" + Fore.CYAN + "IIIIIIIIIIIIIIIIIIIIIIIIII" + Fore.BLUE + "$$$$$" + Fore.RESET)
    print(Fore.BLUE + "           $$$$$" + Fore.CYAN + "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIII" + Fore.BLUE + "$$$$" + Fore.RESET)
    print(Fore.BLUE + "          $$$$$" + Fore.CYAN + "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII" + Fore.BLUE + "$$$" + Fore.RESET)
    print(Fore.BLUE + "         $$$$$" + Fore.CYAN + "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII" + Fore.BLUE + "$$$$" + Fore.RESET)
    print(Fore.BLUE + "        Z$$$$" + Fore.CYAN + "IIII" + Fore.WHITE + ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,," + Fore.CYAN + "III" + Fore.BLUE + "$$$" + Fore.RESET)
    print(Fore.BLUE + "        $$$$" + Fore.CYAN + "IIIII" + Fore.WHITE + "================================" + Fore.CYAN + "III" + Fore.BLUE + "$$$$" + Fore.RESET)
    print(Fore.BLUE + "        $$$$" + Fore.CYAN + "IIIII" + Fore.WHITE + ",,,,,,,,,,,,,Richy,,,,,,,,,,,,,," + Fore.CYAN + "7III" + Fore.BLUE + "$$$" + Fore.RESET)
    print(Fore.BLUE + "        $$$$" + Fore.CYAN + "IIIII" + Fore.WHITE + "================================" + Fore.CYAN + "IIII" + Fore.BLUE + "$$$" + Fore.RESET)
    print(Fore.BLUE + "        $$$$" + Fore.CYAN + "IIIII" + Fore.WHITE + ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,," + Fore.CYAN + "7III" + Fore.BLUE + "$$$" + Fore.RESET)
    print(Fore.BLUE + "        $$$$" + Fore.CYAN + "IIIII" + Fore.WHITE + "================================" + Fore.CYAN + "IIII" + Fore.BLUE + "$$$" + Fore.RESET)
    print(Fore.BLUE + "        $$$$" + Fore.CYAN + "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII" + Fore.BLUE + "$$$$" + Fore.RESET)
    print(Fore.BLUE + "         $$$$$" + Fore.CYAN + "IIII" + Fore.WHITE + ",,,,,,,,,,,,,,," + Fore.CYAN + "IIIIIIIIIIIIIIIIIII" + Fore.BLUE + "$$$$" + Fore.RESET)
    print(Fore.BLUE + "         $$$$$" + Fore.CYAN + "I7II" + Fore.WHITE + "===============" + Fore.CYAN + "IIIIIIIIIIIIIIIIII" + Fore.BLUE + "$$$$" + Fore.RESET)
    print(Fore.BLUE + "          $$$$$" + Fore.CYAN + "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII" + Fore.BLUE + "$$$$$" + Fore.RESET)
    print(Fore.BLUE + "            $$$$$" + Fore.CYAN + "IIIIIIIIIIIIIIIIIIIIIIIIIIIIII7" + Fore.BLUE + "$$$$$$" + Fore.RESET)
    print(Fore.BLUE + "             $$$$$" + Fore.CYAN + "IIIIIIIIIIIIIIIIIIIIIIIIIIIII7" + Fore.BLUE + "$$$$$" + Fore.RESET)
    print(Fore.BLUE + "              $$$$$$" + Fore.CYAN + "7IIIIIIIIIIIIIIIIIIIIIIII" + Fore.BLUE + "$$$$$$ " + Fore.RESET)
    print(Fore.BLUE + "                 $$$$$$$$" + Fore.CYAN + "IIIIIIIIIIIIIII" + Fore.BLUE + "$$$$$$$$$" + Fore.RESET)
    if show_version == "True":
        print(Fore.BLUE + "                     $$$$$$$$$$$$$$$$$$$$$$$" + Fore.WHITE + "     0.50_Beta")
    elif show_version == "False":
        print(Fore.BLUE + "                     $$$$$$$$$$$$$$$$$$$$$$$" + Fore.RESET)
    else:
        print(Fore.BLUE + "Richy: " + Fore.RED + "Invalid show_version value. Please change it to True or False in config.")
        print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting...")
        sys.exit()


def medium(show_version, coloured_version, letter_color):


    """ Setting up the colour of the letters and printing the text in it """
    init()
    if letter_color == "BLUE" or letter_color == "Blue" or letter_color == "blue":
        color_changer = Fore.BLUE
    elif letter_color == "GREY" or letter_color == "Grey" or letter_color == "grey":
        color_changer = Fore.GREY
    elif letter_color == "PINK" or letter_color == "Pink" or letter_color == "pink":
        color_changer = Fore.PINK
    elif letter_color == "YELLOW" or letter_color == "Yellow" or letter_color == "yellow":
        color_changer = Fore.YELLOW
    elif letter_color == "GREEN" or letter_color == "Green" or letter_color == "green":
        color_changer = Fore.GREEN
    elif letter_color == "RED" or letter_color == "Red" or letter_color == "red":
        color_changer = Fore.RED
    elif letter_color == "WHITE" or letter_color == "White" or letter_color == "white":
        color_changer = Fore.WHITE
    else:
        print(Fore.BLUE + "Richy: " + Fore.RED + "Invalid letter_color value. Please change it in config and restart Richy.")
        print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting...")
        sys.exit()

    print("\n")
    print(color_changer + "                     ooooooooo.    o8o            oooo                     " + Fore.RESET)
    print(color_changer + "                     `888   `Y88.  `''            `888                     " + Fore.RESET)
    print(color_changer + "                      888   .d88' oooo   .ooooo.   888 .oo.   oooo    ooo  " + Fore.RESET)
    print(color_changer + "                      888ooo88P'  `888  d88' `'Y8  888P'Y88b   `88.  .8'   " + Fore.RESET)
    print(color_changer + "                      888`88b.     888  888        888   888    `88..8'    " + Fore.RESET)
    print(color_changer + "                      888  `88b.   888  888   .o8  888   888     `888'     " + Fore.RESET)
    print(color_changer + "                     o888o  o888o o888o `Y8bod8P' o888o o888o     .8'      " + Fore.RESET)
    if show_version == "True":
        if coloured_version == "True":
            print(color_changer + "                                                               .o..P'     0.50_Beta  " + Fore.RESET)
        elif coloured_version == "False":
            print(color_changer + "                                                               .o..P'    " + Fore.WHITE + " 0.50_Beta  " + Fore.RESET)
        else:
            print(Fore.BLUE + "Richy: " + Fore.RED + "Invalid coloured_version value. Please change it to True or False in config.")
            print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting...")
            sys.exit()
    elif show_version == "False":
        print(color_changer + "                                                               .o..P'      " + Fore.RESET)
    else:
        print(Fore.BLUE + "Richy: " + Fore.RED + "Invalid letter_color value. Please change it in config and restart Richy.")
        print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting...")
        sys.exit()

def large(show_version, coloured_version, letter_color):

    """ Setting up the colour of the letters and printing the text in it """
    init()
    if letter_color == "BLUE" or letter_color == "Blue" or letter_color == "blue":
        color_changer = Fore.BLUE
    elif letter_color == "GREY" or letter_color == "Grey" or letter_color == "grey":
        color_changer = Fore.GREY
    elif letter_color == "PINK" or letter_color == "Pink" or letter_color == "pink":
        color_changer = Fore.PINK
    elif letter_color == "YELLOW" or letter_color == "Yellow" or letter_color == "yellow":
        color_changer = Fore.YELLOW
    elif letter_color == "GREEN" or letter_color == "Green" or letter_color == "green":
        color_changer = Fore.GREEN
    elif letter_color == "RED" or letter_color == "Red" or letter_color == "red":
        color_changer = Fore.RED
    elif letter_color == "WHITE" or letter_color == "White" or letter_color == "white":
        color_changer = Fore.WHITE
    else:
        print(Fore.BLUE + "Richy: " + Fore.RED + "Invalid letter_color value. Please change it in config and restart Richy.")
        print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting...")
        sys.exit()

    print("\n")
    print(color_changer + "                                        ooooooooo.    o8o            oooo                     " + Fore.RESET)
    print(color_changer + "                                        `888   `Y88.  `''            `888                     " + Fore.RESET)
    print(color_changer + "                                         888   .d88' oooo   .ooooo.   888 .oo.   oooo    ooo  " + Fore.RESET)
    print(color_changer + "                                         888ooo88P'  `888  d88' `'Y8  888P'Y88b   `88.  .8'   " + Fore.RESET)
    print(color_changer + "                                         888`88b.     888  888        888   888    `88..8'    " + Fore.RESET)
    print(color_changer + "                                         888  `88b.   888  888   .o8  888   888     `888'     " + Fore.RESET)
    print(color_changer + "                                        o888o  o888o o888o `Y8bod8P' o888o o888o     .8'      " + Fore.RESET)
    print(color_changer + "                                                                                  .o..P'      " + Fore.RESET)

    if show_version == "True":
        if coloured_version == "True":
            print(color_changer + "                                                                                  .o..P'       0.50_Beta  " + Fore.RESET)
        elif coloured_version == "False":
            print(color_changer + "                                                                                  .o..P'      " + Fore.WHITE + " 0.50_Beta  " + Fore.RESET)
        else:
            print(Fore.BLUE + "Richy: " + Fore.RED + "Invalid coloured_version value. Please change it to True or False in config.")
            print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting...")
            sys.exit()
    elif show_version == "False":
        print(color_changer + "                                                                                  .o..P'      " + Fore.RESET)
    else:
        print(Fore.BLUE + "Richy: " + Fore.RED + "Invalid letter_color value. Please change it in config and restart Richy.")
        print(Fore.BLUE + "Richy: " + Fore.RED + "Exiting...")
        sys.exit()


# -----------------------------------  Main  -----------------------------------

if __name__ == '__main__':
    pass
