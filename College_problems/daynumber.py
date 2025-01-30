"""
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return
the day number of the year.

Example 1:
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.

Example 2:
Input: date = "2019-02-10"
Output: 41
"""
def isleap(n):
    if n%4 == 0 and n%100 != 0 or n%400 == 0:
        return True
    else:
        return False

def dayofyear(date):
    yr = int(date[0:4])
    m = int(date[5:7])
    d = int(date[8::])
    days = 0
    for i in range(1,m): # Iterate till this month
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 11 or i == 12: # Check for months with 31 days
            days += 31
        elif i == 4 or i == 6 or i == 9 or i == 10: # check for months with 30 days
            days += 30
        else:
            if isleap(yr): # check for leap year for days in feb
                days += 29
            else:
                days += 28
    days += d # add this month's days
    return days

if __name__ == "__main__":
    print(dayofyear("2019-12-10"))