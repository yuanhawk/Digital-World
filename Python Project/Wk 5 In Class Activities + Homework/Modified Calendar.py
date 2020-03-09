# NB: the following line imports the 'display_calendar', 'lear_year', etc. functions
# (see the problem sheet PDF)
# DO NOT delete hw2_others.pyc from Vocareum :-)
from hw2_others import *

# You should ONLY submit the 'display_calendar_modified' function

def display_calendar_modified(year, month_num):
    if month_num == None:
        return display_calendar(year)
    
    list_of_str_year = construct_cal_year(year)
    cal_year = [list_of_str_year[0], list_of_str_year[month_num]]
    cal_year.pop(0)
    
    cal = ''
    for i, month in enumerate(cal_year):
        for i, week in enumerate(month):
            cal += week + '\n'
            if i == 0:
                cal += '  S  M  T  W  T  F  S\n'
        if i != 11:
            cal += '\n'
    return cal.strip()