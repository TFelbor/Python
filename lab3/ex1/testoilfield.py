from ex1.oilfield import *

filepath = input("Enter the path of the data file: ").strip()
of = OilField(filepath)
y = of.find()
pipelen = of.pipelength()

print("The main pipeline is the line y =",y)
print("The total pipeline length is {:1.2f}".format(pipelen))