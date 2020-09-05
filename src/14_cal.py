"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

inputs = []

for arg in sys.argv:
  inputs.append(arg)

currentMonth = int(str(datetime.now())[5:7])

currentYear = int(str(datetime.now())[0:4])

formatErrorMessage = 'Error:\nThis file accepts the following format:\npython3 14_cal.py [month] [year]\nwhere [month] and [year] are optional, but if included must be integer values\n[month]: 1-12\n[year]: 1-9999\nentering only one value will assume the entered value is [month]'

try:
  #check if inputs are numbers
  int(inputs[1])
  int(inputs[2])
except ValueError:
  print(formatErrorMessage)
  sys.exit(1)
except IndexError:
  pass


#check if there are too many inputs
if (len(inputs) <= 3):

  if (len(inputs) == 2):
    if (1 <= int(inputs[1]) <= 12):
      print(calendar.month(currentYear, int(inputs[1])))
    else: 
      print(formatErrorMessage)

  elif (len(inputs) == 3):
    if ((1 <= int(inputs[1]) <= 12) and (1 <= int(inputs[2]) <= 9999)):
      print(calendar.month(int(inputs[2]), int(inputs[1])))
    else:
      print(formatErrorMessage)

  else:
    print(calendar.month(currentYear, currentMonth))

else:
  print(formatErrorMessage)
