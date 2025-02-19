# Question 1 What is the result?

a = 10

a = a + 2

print(a*2)

a = 19

print(a+3)

a = a // 2

# Question 2
print(2+3*6/2)

# Question 3

import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)