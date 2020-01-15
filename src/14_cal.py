"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
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
"""

import sys
import calendar
from datetime import datetime

def myCal():
  #Importing today's date for ease of use
  today = datetime.today()

  #The file name 14_cal.py counts as the first arg
  if len(sys.argv) == 1:
  #Returns todays month & year if no argument is passed
    print(calendar.month(today.year, today.month))
  #Passes arg to month
  elif len(sys.argv) == 2:
    print(calendar.month(today.year, int(sys.argv[1])))
  #Passes first arg to month and second to year
  elif len(sys.argv) == 3:
    print(calendar.month(int(sys.argv[2]), int(sys.argv[1])))
  else:
      print("Please enter number of the month and year you wish to display.")


myCal()