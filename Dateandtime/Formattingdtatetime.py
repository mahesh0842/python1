import datetime

x = datetime.datetime.now()

print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%d"))
print(x.strftime("%Y"))
print(x.strftime("%H"))
print(x.strftime("%M"))# Minutes
print(x.strftime("%S"))# Seconds
print(x.strftime("%p"))# AM or PM
print(x.strftime("%I"))# Hour in 12-hour format
print(x.strftime("%j"))# Day of the year
print(x.strftime("%U"))# Week number of the year (Sunday as the first day of the week)
print(x.strftime("%W"))# Week number of the year (Monday as the first