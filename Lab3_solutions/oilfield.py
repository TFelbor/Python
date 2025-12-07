from oilwell import *

class OilField:

    # returns an oil field containing the oiwells
    # defined in the CSV file of path 'filepath'
    def __init__(self ,filepath):
        file = open(filepath ,'r')
        self._owl = []
        for line in file:
            line = line.strip().split(",")
            self._owl.append(OilWell(float(line[1]) ,float(line[2]) ,line[0]))
        file.close()
        self._owl.sort()

    # returns the coefficient a of the equation y = a
    # describing the position of the main pipeline
    def find(self):
        return self._owl[len(self._owl )//2].ycoord

    # returns the total length of the secondary
    # pipelines to link the oil wells to the main pipeline
    def pipelength(self):
        y = self.find()
        return sum([ abs(ow.ycoord - y) for ow in self._owl ])
