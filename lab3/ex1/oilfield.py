import csv

class OilWell:
    def __init__(self, n, x, y):
        self.name = n
        self.x_dist = float(x)
        self.y_dist = float(y)
    
    def __lt__(self, other):
        return self.y_dist < other.y_dist

class OilField:

    def __init__(self, filename):
        self.oilwells = [] 

        try:
            with open(filename, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    temp_oilwell = OilWell(row[0], row[1], row[2])
                    self.oilwells.append(temp_oilwell)
        except Exception as e:
            print(f"Failed to read file: {e}")

    def find(self):
        if not self.oilwells:
            print("No oilwells found. Cannot calculate median.")
            return 0

        self.oilwells.sort()
        length = len(self.oilwells)
        
        # Odd case
        if (length % 2 == 1):
            middle = int(length / 2)
            return self.oilwells[middle].y_dist
        # Even case
        else:
            middle1 = int(length / 2)
            middle2 = int((length / 2) - 1)
            average = (self.oilwells[middle1].y_dist + self.oilwells[middle2].y_dist) / 2
            return average 

    def pipelength(self):
        if not self.oilwells:
            return 0 
        a_value = self.find()
        total_length = 0
        for oilwell in self.oilwells:
            dist = abs(oilwell.y_dist - a_value)
            total_length += dist
        return total_length

if __name__ == '__main__':
    filename = input("Enter the path of the data file: ").strip()
    o = OilField(filename)
    print(f"The main pipeline is the line y = {o.find()}")
    # Format to 2 decimal places to match your example output
    print(f"The total pipeline length is {o.pipelength():.2f}")