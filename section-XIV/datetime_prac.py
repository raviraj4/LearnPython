import datetime as dt
# datetime module has datetime class 
d = dt.datetime(year=2024,month=2, day=3)
t = dt.time(2,2,2)
f = dt.time(3,20,10)
print(f'{t} \t {d}')
# timedelta is to calculate difference 
a = d - dt.timedelta(2)
print(f"timedelta: {a}")

