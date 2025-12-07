from simpledate import SimpleDate

class FullDate(SimpleDate):

    def __init__(self, year, month, day):
        SimpleDate.__init__(self, month, day)
        self.year = year

    def __str__(self):
        return str(self.year) + "/" + super().__str__()

    def copy(self):
        return FullDate(self.year, self.month, self.day)

    def __eq__(self, other):
        return self.year == other.year and super().__eq__(other)

    def __lt__(self, other):
        if self.year == other.year:
            return super().__lt__(other)
        else:
            return self.year < other.year

    def __gt__(self, other):
        if self.year == other.year:
            return super().__gt__(other)
        else:
            return self.year > other.year

    def daysinmonth(self):
        if self.month == 2 and self._leapyear():
            return 29
        return super().daysinmonth()

    def nextday(self):
        super().nextday()
        if self.day == 1 and self.month == 1:
            self.year += 1

    def daystodate(self, date):
        if self == date:
            return 0
        if self < date:
            return super().daystodate(date)
        return date.daystodate(self)

    def _leapyear(self):
        return self.year % 4 == 0 and ( self.year % 100 != 0 or self.year % 400 == 0 )