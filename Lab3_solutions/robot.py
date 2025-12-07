from context import *

class Found(Exception):
    """
    This class is raised when a robot finds the goal.
    """
    pass

class Robot(object):

    def __init__(self, context):
        """
        Creates a robot with given context.
        :param context: the context of the robot
        """
        self.context = context
        self.x = 0
        self.y = 0

    def reachable(self, direction):
        """
        Checks if the robot can reach the neighbor cell
        :param direction: the direction of the neighbor cell
        """
        return self.context.reachable(direction)

    def move(self, direction):
        """
        Moves the robot to the neighbor cell of the given direction
        :param direction: the direction of the neighbor cell
        """
        self.context.move(direction)
        if direction == Direction.NORTH:
            self.y += 1
        elif direction == Direction.EAST:
            self.x += 1
        elif direction == Direction.SOUTH:
            self.y -= 1
        else:
            self.x -= 1
        print("go " + direction.name)

    def possible_directions(self):
        directions = []
        for direction in Direction:
            if self.reachable(direction):
                directions.append(direction)
        return directions

    def neighbor_node(self, direction):
        if direction == Direction.NORTH:
            return self.x, self.y+1
        if direction == Direction.EAST:
            return self.x+1, self.y
        if direction == Direction.SOUTH:
            return self.x, self.y-1
        if direction == Direction.WEST:
            return self.x-1, self.y

    def find_goal(self):
        """
        Moves the robot until it finds the goal.
        The robot must print out all the steps
        it takes on its way
        """
        visited = set()
        try:
            self.explore_path(visited)
        except Found:
            print("Found!!")
        else:
            print("Damned, no exit!!")

    def explore_path(self, visited):
        if self.context.isgoal():
            raise Found
        current = self.x, self.y
        visited.add(current)
        for direction in self.possible_directions():
            n = self.neighbor_node(direction)
            if n not in visited:
                self.move(direction)
                self.explore_path(visited)
                self.move(direction.opposite())

def main():
    r2d2 = Robot(context1)
    r2d2.find_goal()

if __name__ == "__main__":
    main()
