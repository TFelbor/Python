class OilWell:

    # returns an oilwell of position ('x','y')
    # and name 'name'
    def __init__(self, x, y, name):
        self._x, self._y, self._name = x, y, name

    # returns the x coordinate of self
    @property
    def xcoord(self):
        return self._x

    # returns the y coordinate of self
    @property
    def ycoord(self):
        return self._y

    # returns the name of self
    @property
    def name(self):
        return self._name

    # checks if self is less than ow
    # (YOU MUST DEFINE WHAT IT MEANS!!)
    def __lt__(self, ow):
        if self._y == ow._y:
            return self._x < ow._x
        return self._y < ow._y

    # returns a string representation of self
    # in the form "NAME(x,y)"
    def __repr__(self):
        return "{}({:1.2f},{:1.2f})".format(self._name, self._x, self._y)
