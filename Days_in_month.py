# Print a number of days in a month.

def number_of_days(year,month):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month==2 and (year%4==0 or year%100==0 and year%400==0):
        return 29
    else:
        return days[month-1]

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

print(number_of_days(year,month))