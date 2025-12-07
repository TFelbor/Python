class SimpleDate:

    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.month}/{self.day}"

    def copy(self):
        return SimpleDate(self.month, self.day)

    def __eq__(self, other):
        return self.month == other.month and self.day == other.day

    def __lt__(self, other):
        if self.month == other.month:
            return self.day < other.day
        else:
            return self.month < other.month

    def __gt__(self, other):
        if self.month == other.month:
            return self.day > other.day
        else:
            return self.month > other.month

    def daysinmonth(self):
        dim = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        return dim[self.month - 1]

    def nextday(self):
        if self.day == self.daysinmonth():
            self.day = 1
            if self.month == 12:
                self.month = 1
            else:
                self.month += 1
        else:
            self.day += 1

    def daystodate(self, date):
        tmp = self.copy()
        nod = 0
        while tmp < date:
            tmp.nextday()
            nod += 1
        return nod
