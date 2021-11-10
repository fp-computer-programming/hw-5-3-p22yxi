# Author Yongdong Xi (Nov 2)
import calendar

# Question 1
calendar.TextCalendar().pryear(2020)

# Question 2
calendar.TextCalendar(6).pryear(2020)

# Question 3
year = 2002
month = 1
x = calendar.month(year, month)
print(x)

# Question 4
calendar.LocaleTextCalendar(6, "CHINSESE").pryear(2020)

# Question 5
calendar.isleap(2002)
print("This is Boolean tpye，it works for find leap year")
