# Richy
Personal assistant made especially for GNU/Linux because we deserve our own version of Siri too!


Did you ever wanted to have your own assistant, but the only ones available are for Android/iOS/Windows plus you are
worried about privacy?

Well, now you can have '**Richy**' which will help you to live in the terminal, because what's the point of searching the web (which can take a while by the way) when you can simply just ask Richy?

Richy is open-source python-based assistant which can help you with;
- maintaining your schedule,
- aswering your questions,
- calculating medium-level calculation,
- giving you informations about your movies library or any movie you want

## Curent version

The most recent version _0.50 Beta_ brings:

 - (Change) The code has been rewritten to allow publishing to Github

## Warning!

Richy in its current form still has multiple bugs and errors that I will be fixing over time. If you found some
bugs in the code or you have more efficient way of performing a task, just create new issue in the [issue tracker](https://github.com/michpcx/Richy/issues).

## Installation
After downloading Richy, move folder richy to /home/your-user-name-here/ and change its name to .richy. After that you can simply just run richy_main.py to run the program. If you choose to install Richy so you don't need to run the script each time, run setup.py.

## Basic questions
```
'schedule'
'whats 100*42?'
'tell me a joke'
'26 pounds to kg'
'rhymes with coder'
'dictionary vehicle'
'scrabble programming'
'US $900 2005' (inflation)
'december 30, 1990 plus 10000 days'
```

## To-do
- [x] *Search for movies on the hard drive and give info about them*
- [x] *Move commands into the file*
- [x] *Currency conversion*
- [x] *Random jokes*
- [x] *Dictionary*
- [ ] *Wikipedia*
- [ ] *Show weather*
- [ ] *Random fact/quotes*
- [ ] *Improve calculator*
- [ ] *Lyrics for chosen song*
- [ ] *Url expander/shortener*
- [ ] *News from chosen websites*
- [ ] *Allow to install Heinrichy*
- [ ] *Download subtitles for movies*
- [ ] *Give tvshow/book/music description*

## Modules

Prebuilded modules which you can find in Richy;
- Schedule (external) - allows to modify your schedule which will then be displayed in Richy ('schedule')
- Multimedia (internal) - allows to get more information about movies you have on the local drive ('movie help')

And many more modules and features coming soon!

## Why Richy?
Name 'Richy' is a modification after the name of famous physicist [Heinrich Friedrich Weber](https://en.wikipedia.org/wiki/Heinrich_F._Weber) which was Albert Einstein's initial doctoral
advisor. As Heinrich was helping Albert Einstein, Richy will help you with day-to-day questions and tasks.
It was made especially for GNU/Linux as members of Linux family also need an assistant, however with few
code modifications, the code should work on Microsoft Windows or MacOS. I've decided to create Richy after
I came across an article where the author was trying to live in the terminal and only use the terminal without any GUI for
30 days. This is nearly impossible without any preparation which is why I created Richy, I wanted to do
nearly everything in the command line without the need for any user interface.

## Release notes

--------------------------------- 0.50_Beta -----------------------------------  (10th of September 2019)

 - (Change) The code has been rewritten to allow publishing to Github
 
 --------------------------------- 0.45_Beta -----------------------------------  (16th of August 2016)

 - (Change) Changed name "Heinrichy" to just "Richy" which makes it simpler and easier to remember.
 - (Change) Code has been optimized for stability
 - (Change) Richy has entered Beta phrase and left Alpha as it works quite well without giving many errors
 - (+) Added ability to install Richy using setup.py script (you can then just run 'richy what day is it' and richy will give you the answer.
 - (Change) Richy config and modules has been moved to /home/$USER/.richy
 - (+) Added ability to change the size of terminal in config which will change the main "Richy" text to fit the size of terminal that has been chosen.
 - (+) Added ability to colour in version of Richy if you choose to dispaly it.
 - (+) Created logo_printer.py script which holds the functions for printing out the logo.
 - (+) Added better exception handling
 - (+) Created script which will run the first time Richy is being run to modify the config, so the user can input his/hers name etc.
 - (+) Added wikipedia summary (can be used as 'wiki the hobbit' for example)

 --------------------------------- 0.38_Alpha -----------------------------------  (12th of August 2016)

 - (Change) Changed class with colours to 'colorama' module as colorama has wider range of options
 - (Change) Moved config.conf, schedule.json and movies_list.json to config file
 - (Change) Moved commands to data.json in config folder so its easier to check for commands and there can be lots of variations like "schedule" and "show me my schedule" etc.
 - (Change) Changed how Heinrichy shows schedule so it is updated every time it wants to show it

--------------------------------- 0.36_Alpha -----------------------------------  (11th of August 2016)

- (+) Added ability to search for single movie online using command 'movie search (the movie title)'
- (Fix) Fixed error handling when user searches for single movie

--------------------------------- 0.35_Alpha -----------------------------------  (6th of August 2016)

- (Change) Changed config format from py to conf (loading using configparser) for flexibility
- (+) Added ability to turn on/off schedule module, multimedia module and modules that will come in the future
- (+) New module called multimedia which allows to give you more info about movies you have on the local hard drive
- (+) Created first_timer.py script which checks if you have required packages installed to run Heinrichy

--------------------------------- 0.27_Alpha -----------------------------------  (24th of July 2016)

- (Change) Converted few lines of code into python-3 compatible so Heinrichy can be run now on both versions of python; 2.7 & 3.*
- (-) Removed environment.py as it was crashing in python 3
- (-) Removed ability to change the version of Heinrichy in config
- (Change) Moved schedule to separate file schedule.json

--------------------------------- 0.23_Alpha -----------------------------------  (20th of July 2016)

- (+) Added ability to search Evi (www.evi.com) if wolframalpha servers return error/no response
- (+) The user has now the ability to change if the searches will be directed automatically to Evi if wolframalpha returns error, to ask every time or to never contact Evi.
- (Fix) Fixed bug with schedule list being repeated after opening and exiting schedule module
- (Added) From now on, Heinrichy is shared under GLP v3 license.
- (Added) Users now can change the format of the dates in the config

--------------------------------- 0.20_Alpha -----------------------------------  (10th of July 2016)

- (Change) The whole script was rewritten so the code is more elegant and its not a mess.
- (Change) Config file was changed from json format to py.
- (+) Created environment.py to check the os and python version on startup.
- (Change) Schedule now will be managed as separate module in /modules.
- (+) Added ability to change the colour of the "Heinrichy" text
- (+) Added ability to remove schedule from showing up after the "Heinrichy" text
- (+) Added ability to clear the screen after output from Heinrichy
- (Change) Moved main 'Heinrichy' text and schedule view to the functions

--------------------------------- 0.11_Alpha -----------------------------------  (18th of January 2016)

- (-) Deleted few lines of code in data.py that weren't needed.
- (+) Added few sentence modifications that allow to add schedule.
- (Change) Moved birthday checking to function.
- (Change) Ask Heinrichy how old he is.
- (Fix) Fixed bug with signs "--" that were doubled if there wasn't any events for today.


--------------------------------- 0.10_Alpha -----------------------------------  (18th of January 2016)

- (+) Added function to add tasks to the schedule.
- (Change) Variable local_command set as global at the start of the function instead at the end.


## How can I help?

If you have any ideas on how Richy could be improved or if you found some interesting
script that could be used as module to Richy, just email me; michpcx@protonmail.ch. Also, if you found some
bugs in the code or you have more efficient way of performing a task, just create new issue in the [issue tracker](https://github.com/michpcx/Richy/issues).

*By michpcx, michpcx@protonmail.ch*
