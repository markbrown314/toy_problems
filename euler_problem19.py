"""
Euler #19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def num_days_in_month(month, year):
        if month == 9 or month == 4 or month == 6 or month == 11:
            return 30
        if month == 2:
            if year % 4 == 0:
                if year % 400 != 0:
                    return 29
            return 28
        # other months
        return 31

# range from 1 jan 1900 to 1 Jan 2001
day = 0
sunday_count = 0
for year in range(1900, 2000+1):
    print("year:",year)
    for month in range(1, 12+1):
        print("month:", month)
        day = day + num_days_in_month(month, year)
        print("day:", day)
        if year == 2000 and month == 12:
            break
        if day % 7 == 0:
            if year > 1900:
                sunday_count +=1

print("sunday count #", sunday_count)
