import time
import sys

print()
print("Jay's countdown timer")
print()

c = ':'

print()
years = input("Years:  ")
months = input("Months:  ")
days = input("Days:  ")
hours = input("Hours: ")
mins = input("Minutes: ")
secs = input("Seconds: ")
print()

hour = int(hours)
min = int(mins)
sec = int(secs)
day = int(days)
month = int(months)
year = int(years)

while year > -1:
    while month > -1:
        while day > -1:
            while hour > -1:
                while min > -1:
                    while sec > 0:
                        sec = sec - 1
                        time.sleep(1)
                        sec1 = ('%02.f' % sec)
                        min1 = ('%02.f' % min)
                        hour1 = ('%02.f' % hour)
                        day1 = ('%02.f' % day)
                        month1 = ('%02.f' % month)
                        year1 = ('%02.f' % year)
                        sys.stdout.write('\r' + str(year1) + c + str(month1) + c + str(day1) + c + str(hour1) + c + str(min1) + c + str(sec1))

                    min = min -1
                    sec = 59
                hour = hour - 1
                min = 59
            day = day - 1
            hour = 23
        month = month - 1
        day = 29
    year = year - 1
    month = 11

print()
print('Countdown Complete!!!')
time.sleep(10)