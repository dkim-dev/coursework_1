#!/usr/bin/env python3

''' OPS435 Assignment 1 - Winter 2020
Program: a1_dkim151.py (replace student_id with your Seneca User name)
Author: "Danil Kim"
The python code in this file (a1_dkim151.py) is original work written by
"Danil Kim". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''

import sys

def leap_year(year):

    '''The module 'leap_year' calculates if a year provided by user is a leap year'''

    if year % 4 == 0:
        return True # this is a leap year
    elif year % 100 == 0:
        return False # this is not a leap year
    elif year % 400 == 0:
        return True # this is a leap year

def days_in_mon(yvalue):

    '''
    Module 'days_in_mon' takes return from the 'leap_year' module and makes change to amount of day in February
    '''

    if leap_year(yvalue):
        feb = 29
    else:
        feb = 28

    mon_max = { 1:31, 2:feb, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    return mon_max

def after(day):

    ''' 
    Code of the 'after' module adds a number of days to a date
    '''
    
    valid_date(day)
    str_year, str_month, str_day = day.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    mon_max = days_in_mon(year)
    next_day = day + 1

    if next_day > mon_max[month]: 
        next_day = 1
        month = month + 1

        if month > 12:
            month = 1
            year = year + 1

    next_date = (str(year)+'-'+str(month).zfill(2)+'-'+str(next_day).zfill(2))

    return next_date

def before(var1):

    '''
    Code of the 'before' module substracts a number of days from a date
    '''
    valid_date(var1)
    str_year, str_month, str_day = var1.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    mon_max = days_in_mon(year)
    before_day = day - 1

    if before_day == 0:
        month = month - 1
        if month == 0:
            year = year -1
            month = 12
            before_day = 31
        else:
            before_day = mon_max[month]

    day_before = (str(year)+'-'+str(month).zfill(2)+'-'+str(before_day).zfill(2))

    return day_before

def valid_date(var1):
    '''
    valid_date' module checks if:
    - provided date is in correct format,
    - contains 10 items (including dashes('-'), and
    - the date doesn't go below Oct 1582 (the date when the Gregorian calendar
    was introduced.
    '''
    if (len(var1) != 10):   
        print("Error: wrong date entered")
        exit()

    else:
        str_year, str_month, str_day = var1.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        mon_max = days_in_mon(year)
        if year <= 1582 and month <= 10:
            print("Error: The calendar cannot go below the date of October 1582 (the date when the Gregorian Calendar was introduced to the World)")
            exit()
        if month not in mon_max.keys():
            print("Error: wrong month entered")
            exit()
        else:
            day_max = mon_max[month]
            if day not in range (1,day_max+1):    
                print("Error: wrong day entered")
                exit()

def dbda(var1,var2):
    i = 0
    total = 0
    RemainDay = var1
    if len(str(var2)) == 10:
        valid_date(var2)
        if var1 < var2:
            while RemainDay < var2:  
                total +=1
                RemainDay = after(RemainDay)
        elif var1 > var2:
            while RemainDay > var2:  
                total +=1
                RemainDay = before(RemainDay)

        print(total)    

    else:   
        if int(var2) > 0: 
            while i < int(var2):  
                i += 1
                if sys.argv[1] == '--step':
                    RemainDay = after(RemainDay)
                    print(RemainDay)
                else:
                    RemainDay = after(RemainDay)               
        elif int(var2) < 0:  
            while i > int(var2):
                i = i - 1
                if sys.argv[1] == '--step':
                    RemainDay = before(RemainDay)
                    print(RemainDay)
                else:
                    RemainDay = before(RemainDay)          
        else:
            RemainDay = RemainDay
        if sys.argv[1] == '--step':
            print('\n')
        else:
            print(RemainDay) 

def usage():
    NumberOfArgument = len(sys.argv)
    if ((NumberOfArgument != 4) and NumberOfArgument != 3): 
        print ('Usage: '+sys.argv[0] + ' [--step] YYYY-MM-DD +/-n\r\n'+'Usage2: '+sys.argv[0]+' YYYY-MM-DD YYYY-MM-DD')
        exit()
if __name__ == "__main__":

    usage()

    if sys.argv[1] == '--step':

        var1 = sys.argv[2]

        var2 = sys.argv[3]

    else:

        var1 = sys.argv[1]

        var2 = sys.argv[2]



    dbda(var1,var2)