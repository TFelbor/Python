from context import *
import random

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

    def findgoal(self):
        """
        Moves the robot until it finds the goal.
        The robot must print out all the steps
        it takes on its way
        """
        visited = set()
                
        try:
            # Start the recursive helper
            self.dfs(visited)
        except Found:
            print("Found!!")

    def dfs(self, visited):
            """
            Recursive Depth First Search
            :param visited: A set of (row, col) coordinates already visited
            """
            current_pos = (self.context.row, self.context.col)
            visited.add(current_pos)
            if self.context.isgoal():
                raise Found()
            for direction in Direction:
                if self.reachable(direction):
                    neighbor_pos = self.neighborpos(direction)
                    if neighbor_pos not in visited:
                        print("go ", direction.name)
                        self.move(direction)
                        self.dfs(visited)
                        back = direction.opposite()
                        print("go ", back.name)
                        self.move(back)

    def neighborpos(self, direction):
        """
        FIX 2: Aligned coordinates with Context class
        (North is row-1, East is col+1)
        """
        r, c = self.context.row, self.context.col
        
        if direction == Direction.NORTH:
            return r - 1, c
        elif direction == Direction.SOUTH:
            return r + 1, c
        elif direction == Direction.EAST:
            return r, c + 1
        elif direction == Direction.WEST:
            return r, c - 1
        return r, c
         
    def getmoves(self):
        '''
        Get the possible moves from the current position
        '''
        moves = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
        possible_moves = []
        for move in moves:
            if Context.reachable(move):
                possible_moves.append(move)
        return random.shuffle(possible_moves)


def main():
    r2d2 = Robot(context1)
    r2d2.findgoal()

if __name__ == "__main__":
    main()
