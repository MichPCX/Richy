# -*- coding: UTF-8 -*-

# Richy module info
# [Name] = multimedia
# [Description] = multimedia module allows to manage your library of movies and search for info about movies you don't have
# [Latest update in] = 0.45_Beta


# --------------------------------  Startup  -----------------------------------
""" Importing main modules """
from __future__ import print_function
import os
import sys
import json
import time
import textwrap
import requests
from tqdm import tqdm
from unipath import Path
from guessit import *
from colorama import init, Fore
from terminaltables import AsciiTable
from sys import platform as _platform
try:
    from urllib.parse import urlencode
except:
    from urllib import urlencode



""" Colorama """
init()



""" Importing settings from config file and setting variables """
import configparser
current_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.expanduser("~/.richy/config")
modules_path = os.path.expanduser("~/.richy/modules")
config_file = config_path + "/config.conf"
movies_list_file = config_path + "/movies_list.json"
config = configparser.ConfigParser()
config.read(config_file)
movie_directory = config.get('multimedia_module', 'movie_directory')
date_format = config.get('schedule_module', 'schedule_date_format')
exit_code = 0
todays_date = str(time.strftime("%d/%m/%Y"))
OMDB_URL = 'http://www.omdbapi.com/?'
EXT = (".3g2 .3gp .3gp2 .3gpp .60d .ajp .asf .asx .avchd .avi .bik .bix"
       ".box .cam .dat .divx .dmf .dv .dvr-ms .evo .flc .fli .flic .flv"
       ".flx .gvi .gvp .h264 .m1v .m2p .m2ts .m2v .m4e .m4v .mjp .mjpeg"
       ".mjpg .mkv .moov .mov .movhd .movie .movx .mp4 .mpe .mpeg .mpg"
       ".mpv .mpv2 .mxf .nsv .nut .ogg .ogm .omf .ps .qt .ram .rm .rmvb"
       ".swf .ts .vfw .vid .video .viv .vivo .vob .vro .wm .wmv .wmx"
       ".wrap .wvx .wx .x264 .xvid")
EXT = tuple(EXT.split())



""" Making it 2.7 & 3.5 compatible """
try:
    # Python2
    input = raw_input
    range = xrange
except NameError:
    # Python3
    pass



""" Setting up dictionaries """
movies = []
movie_name = []
not_a_movie = []
movie_not_found = []



""" Setting up format of the dates """
if date_format.lower() == "dd/mm/yyyy":
    schedule_date_format_type = 1
    formatted_date = todays_date
elif date_format.lower() == "mm/dd/yyyy":
    schedule_date_format_type = 2
    formatted_date = todays_date[3:5] + "/" + todays_date[0:2] + "/" + todays_date[6:10]
elif date_format.lower() == "yyyy/mm/dd":
    schedule_date_format_type = 3
    formatted_date = todays_date[6:10] + "/" + todays_date[3:5] + "/" + todays_date[0:2]
elif date_format.lower() == "yyyy/dd/mm":
    schedule_date_format_type = 4
    formatted_date = todays_date[6:10] + "/" + todays_date[0:2] + "/" + todays_date[3:5]
else:
    print("Invalid date format, please change 'schedule_date_format' in config file...")
    print("Exiting...")
    sys.exit()



# --------------------------------  Functions  ---------------------------------
def index_all():
    """ Index all the movies found in specified path """
    print("\n\nIndexing all movies inside " + movie_directory + "\n\n")
    scan_dir()
    if movie_name:
        if movie_not_found:
            print("\n\nData for the following movie(s) could not be fetched -\n")
            for val in movie_not_found:
                print(Fore.RED + val)
        if not_a_movie:
            print(Fore.WHITE + "\n\nThe following media in the folder is not movie type (maybe its a tv show?) -\n")
            for val in not_a_movie:
                print(Fore.RED + val)
        print(Fore.WHITE + "\n\nNow you can run 'movies list' to view them and sort them.")
    else:
        print(Fore.WHITE + "\n\nGiven directory does not contain movies. Pass a directory containing movies\n\n")



def scan_dir():
    """ Scan folder(s) for movies """
    for root, dirs, files in tqdm(os.walk(movie_directory)):
        for name in files:
            path = os.path.join(root, name)
            if os.path.getsize(path) > (25*1024*1024):
                ext = os.path.splitext(name)[1]
                if ext in EXT:
                    movie_name.append(name)

    with tqdm(total=len(movie_name), leave=True, unit='B',
              unit_scale=True) as pbar:
        for name in movie_name:
            data = get_movie_info(name)
            pbar.update()
            if data is not None and data['Response'] == 'True':
                for key, val in data.items():
                    if val == "N/A":
                        data[key] = "-"
                movies.append(data)
            else:
                if data is not None:
                    movie_not_found.append(name)
        with open(movies_list_file, "w") as out:
            json.dump(movies, out, indent=2)

def get_movie_info(name):
    """Find movie information"""
    movie_info = guessit(name)
    if movie_info['type'] == "movie":
        if 'year' in movie_info:
            try:
                return omdb(movie_info['title'], movie_info['year'])
            except KeyError:
                print("Seems like the title you provided is invalid...")
        else:
            try:
                return omdb(movie_info['title'], None)
            except KeyError:
                print("Seems like the title you provided is invalid...")
    else:
        not_a_movie.append(name)

def omdb(title, year):
    """ Fetch data from OMDB API. """
    params = {'t': title.encode('ascii', 'ignore'),
              'plot': 'full',
              'type': 'movie',
              'tomatoes': 'true'}

    if year:
        params['y'] = year

    url = OMDB_URL + urlencode(params)
    return json.loads(requests.get(url).text)

def list_all(args):
    """ List all movies found localy """
    cnt = 0
    for i in range(len(args)):
        if args[i:i+2] == '--':
            cnt += 1
    if cnt > 1:
        print("Sorry but for now, multimedia module accepts only one filter tag at the same time.")
    is_movies_list_file = os.path.isfile(movies_list_file)
    if not is_movies_list_file:
        print("File with list of movies cannot be found, did you run 'movies index'?")
    else:
        if args == "--imdb":
            table_data = [["TITLE", "IMDB RATING"]]
            data, table = butler(table_data)
            for item in data:
                item["Title"] = clean_table(item["Title"], None, item,
                                            table)
                table_data.append([item["Title"], item["imdbRating"]])
            sort_table(table_data, 1, True)

        elif args == "--tomato":
            table_data = [["TITLE", "TOMATO RATING"]]
            data, table = butler(table_data)
            for item in data:
                item["Title"] = clean_table(item["Title"], None, item,
                                            table)
                table_data.append([item["Title"], item["tomatoRating"]])
            sort_table(table_data, 1, True)

        elif args == "--genre":
            table_data = [["TITLE", "GENRE"]]
            data, table = butler(table_data)
            for item in data:
                item["Title"] = clean_table(item["Title"], None,
                                            item, table)
                table_data.append([item["Title"], item["Genre"]])
            sort_table(table_data, 0, False)

        elif args == "--awards":
            table_data = [["TITLE", "AWARDS"]]
            data, table = butler(table_data)
            for item in data:
                item["Title"], item["Awards"] = clean_table(item["Title"],
                                                            item["Awards"], item,
                                                            table)
                table_data.append([item["Title"], item["Awards"]])
            sort_table(table_data, 0, False)

        elif args == "--cast":
            table_data = [["TITLE", "CAST"]]
            data, table = butler(table_data)
            for item in data:
                item["Title"], item["Actors"] = clean_table(item["Title"],
                                                            item["Actors"], item,
                                                            table)
                table_data.append([item["Title"], item["Actors"]])
            sort_table(table_data, 0, False)

        elif args == "--director":
            table_data = [["TITLE", "DIRECTOR(S)"]]
            data, table = butler(table_data)
            for item in data:
                item["Title"], item["Director"] = clean_table(item["Title"],
                                                              item["Director"],
                                                              item, table)
                table_data.append([item["Title"], item["Director"]])
            sort_table(table_data, 0, False)

        elif args == "--year":
            table_data = [["TITLE", "RELEASED"]]
            data, table = butler(table_data)
            for item in data:
                item["Title"] = clean_table(item["Title"], None, item,
                                            table)
                table_data.append([item["Title"], item["Released"]])
            sort_table(table_data, 0, False)

        elif args == "--runtime":
            table_data = [["TITLE", "RUNTIME"]]
            data, table = butler(table_data)
            for item in data:
                item["Title"] = clean_table(item["Title"], None, item,
                                            table)
                table_data.append([item["Title"], item["Runtime"]])
            print_table(table_data)

        elif args == "--imdb-rev":
            table_data = [["TITLE", "IMDB RATING"]]
            data, table = butler(table_data)
            for item in data:
                item["Title"] = clean_table(item["Title"], None, item,
                                            table)
                table_data.append([item["Title"], item["imdbRating"]])
            sort_table(table_data, 1, False)

        elif args == "--tomato-rev":
            table_data = [["TITLE", "TOMATO RATING"]]
            data, table = butler(table_data)
            for item in data:
                item["Title"] = clean_table(item["Title"], None, item,
                                            table)
                table_data.append([item["Title"], item["tomatoRating"]])
            sort_table(table_data, 1, False)
        elif args == "none":
            table_data = [
                ["TITLE", "GENRE", "IMDB", "RUNTIME", "TOMATO",
                 "YEAR"]]
            data, table = butler(table_data)
            for item in data:
                item["Title"], item["Genre"] = clean_table(item["Title"],
                                                           item["Genre"], item,
                                                           table)
                table_data.append([item["Title"], item["Genre"],
                                   item["imdbRating"], item["Runtime"],
                                   item["tomatoRating"], item["Year"]])
            sort_table(table_data, 0, False)
        else:
            print("Wrong filtering tag(s), please try again with different one(s).")


def sort_table(table_data, index, reverse):
    """ Sort the table """
    table_data = (table_data[:1] + sorted(table_data[1:],
                                          key=lambda i: i[index],
                                          reverse=reverse))
    print_table(table_data)

def print_table(table_data):
    """ Print the table """
    table = AsciiTable(table_data)
    table.inner_row_border = True
    if table_data[:1] in ([['TITLE', 'IMDB RATING']],
                          [['TITLE', 'TOMATO RATING']]):
        table.justify_columns[1] = 'center'
    print("\n")
    print(table.table)

def butler(table_data):
    table = AsciiTable(table_data)
    try:
        with open(movies_list_file) as inp:
            data = json.load(inp)
        return data, table
    except IOError:
        print(Fore.WHITE, "\n\nRun `movies index` to index your movies directory.\n\n")

def clean_table(tag1, tag2, item, table):
    """ Clean the table """
    if tag1 and tag2:
        if len(tag1) > table.column_max_width(0):
            tag1 = textwrap.fill(
                tag1, table.column_max_width(0))
            if len(tag2) > table.column_max_width(1):
                tag2 = textwrap.fill(
                    tag2, table.column_max_width(1))
        elif len(tag2) > table.column_max_width(1):
            tag2 = textwrap.fill(
                tag2, table.column_max_width(1))
        return tag1, tag2
    elif tag1:
        if len(tag1) > table.column_max_width(0):
            tag1 = textwrap.fill(
                tag1, table.column_max_width(0))
        return tag1

def movies_help():
    """ Displays help for 'movies' command """
    print("Command 'movies' can help you with organizing your movies library.",
    "Don't know what to watch? Just use one of the filtering tags to search",
    "for best movie in your library! Commands;\n")
    print(Fore.BLUE + "movies index" + Fore.WHITE + " - first command you need to run before using 'movies' command.",
    "It looks for all the movies that it can find in path specified in config and creates",
    "file with list of them.")
    print(Fore.BLUE + "movies list" + Fore.WHITE + " - lists all movies in your library that it can find.")
    print("        " + Fore.GREEN + "--imdb" + Fore.WHITE + " - lists all movies in your library, filtering using imdb reviews.")
    print("        " + Fore.GREEN + "--tomato" + Fore.WHITE + " - lists all movies in your library, filtering using rotten tomatoes reviews.")
    print("        " + Fore.GREEN + "--genre" + Fore.WHITE + " - lists all movies in your library, filtering by genre of the movie.")
    print("        " + Fore.GREEN + "--awards" + Fore.WHITE + " - lists all movies in your library, filtering by the awards the movie got.")
    print("        " + Fore.GREEN + "--director" + Fore.WHITE + " - lists all movies in your library, filtering by the director.")
    print("        " + Fore.GREEN + "--year" + Fore.WHITE + " - lists all movies in your library, filtering by the year it got released.")
    print("        " + Fore.GREEN + "--runtime" + Fore.WHITE + " - lists all movies in your library, filtering by how long is the movie.")
    print("        " + Fore.GREEN + "--imdb-rev" + Fore.WHITE + " - lists all movies in your library, filtering using imdb reviews in the reverse.")
    print("        " + Fore.GREEN + "--tomato-rev" + Fore.WHITE + " - lists all movies in your library, filtering using rotten tomatoes reviews in the reverse.")
    print(Fore.BLUE + "movie(s) search (the name of the movie)" + Fore.WHITE + " - searches for the movie online and gives you info about it.")
    print("\n\nTo give you info about your movies, Richy's multimedia module ",
    "is based on the code from moviemon. Moviemon is a script made by " + Fore.YELLOW + "iCHAIT,"
    " (https://github.com/iCHAIT/moviemon)" + Fore.WHITE + " which allows to search for movies",
    "on the hard drive and get info about them. Big thanks to " + Fore.YELLOW + "iCHAIT" + Fore.WHITE + "!")


def single_movie_info(users_movie_name):
    """ Gives info about single movie """
    if users_movie_name == "":
        print("Movie name not supplied.")
    else:
        data = get_movie_info(users_movie_name)
        if data == None:
            print("Please provide valid movie title...")
        else:
            table_data = [["TITLE", "GENRE", "RELEASED", "RUNTIME", "TOMATO RATING", "IMDB RATING"]]
            table = AsciiTable(table_data)
            try:
                data["Title"] = clean_table(data["Title"], None, data, table)
                table_data.append([data["Title"], data["Genre"], data["Released"], data["Runtime"], data["tomatoRating"], data["imdbRating"]])
                sort_table(table_data, 1, True)

                table_data = [["PLOT"]]
                table = AsciiTable(table_data)
                data["Plot"] = clean_table(data["Plot"], None, data, table)
                table_data.append([data["Plot"]])

                table_data.append(["TRAILER LINK"])
                users_movie_name = users_movie_name.replace(" ", "+")
                TRAILERURL = "https://www.youtube.com/results?search_query=" + users_movie_name + "+trailer"
                table_data.append([TRAILERURL])

                print_table(table_data)


            except KeyError:
                print("Seems like the title you provided is invalid...")
                print("Please provide valid movie title...")


# -----------------------------------  Main  -----------------------------------

if __name__ == '__main__':
    print("multimedia module loaded...")
