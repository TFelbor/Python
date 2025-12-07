from sympy import false

from fulldate import FullDate
from simpledate import SimpleDate

def getdate():
    date = input("enter a date 'm/d' or 'y/m/d': ").strip()
    if date.count('/') > 1:
        y, m, d = date.split('/')
        return FullDate(int(y), int(m), int(d))
    else:
        m, d = date.split('/')
        return SimpleDate(int(m), int(d))

def nomore():
    while True:
        more = input("more ('y' or 'n')? ").lower()
        if more == 'y':
            return False
        if more == 'n':
            return True

print("Day counter\n")
while True:
    date1 = getdate()
    date2 = getdate()
    dtd = date1.daystodate(date2)
    print("There are",dtd,"days between",date1,"and",date2)
    if nomore():
        break
    print()
