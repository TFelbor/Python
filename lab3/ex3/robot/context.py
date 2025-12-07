from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST  = 1
    SOUTH = 2
    WEST  = 3

    def opposite(self):
        """
        Return the opposite direction
        :return: the opposite direction to self
        """
        if self == Direction.NORTH:
            return Direction.SOUTH
        if self == Direction.EAST:
            return Direction.WEST
        if self == Direction.SOUTH:
            return Direction.NORTH
        if self == Direction.WEST:
            return Direction.EAST

class Context(object):

    def __init__(self, grid, row, col, goalrow, goalcol):
        """
        Make a context
        :param grid: the grid
        :param row: the initial row of the robot
        :param col: the initial column of the robot
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.row = row
        self.col = col
        self.goalrow = goalrow
        self.goalcol = goalcol

    def isgoal(self):
        """
        Check if the robot is on the goal cell
        :return: True if the robot is on the goal cell
        """
        return self.row == self.goalrow and self.col == self.goalcol

    def reachable(self,direction):
        """
        Check of the robot can reach a neighbor cell
        :param direction: the direction of the neighbor cell
        :return: True if the robot can reach a neighbor cell
        """
        if direction == Direction.NORTH:
            return self.row-1 >= 0 and self.grid[self.row-1][self.col]
        if direction == Direction.EAST:
            return self.col+1 < self.cols and self.grid[self.row][self.col+1]
        if direction == Direction.SOUTH:
            return self.row+1 < self.rows and self.grid[self.row+1][self.col]
        if direction == Direction.WEST:
            return self.col-1 >= 0 and self.grid[self.row][self.col-1]

    def move(self,direction):
        """
        Move the robot from its current cell to the neighbor cell
        If the neighbor cell in that direction is not reachable, the
        method just print a warning message and does nothing
        :param direction: the direction of the neighbor cell to move to
        """
        if not self.reachable(direction):
            print("can't move in that direction:",direction.name)
            return
        if direction == Direction.NORTH:
            self.row -= 1
        elif direction == Direction.EAST:
            self.col += 1
        elif direction == Direction.SOUTH:
            self.row += 1
        else:
            self.col -= 1

context1 = Context([[True, True, True, False, True],
        [True, False, True, False, True],
        [True, False, True, True, True],
        [True, False, False, False, True],
        [True, True, True, True, True]],4,1, 0, 2)

context2 = Context([[True, True, True, True, True, False, True, True, True, True],
         [True, False, False, False, True, False, False, False, False, True],
         [True, False, True, False, True, True, True, True, True, True],
         [True, False, True, False, True, False, False, False, False, False],
         [False, False, True, False, True, True, True, True, True, True],
         [True, True, True, False, True, False, False, False, False, True],
         [True, False, True, True, True, False, True, True, True, True],
         [True, False, True, False, True, False, True, False, False, True],
         [True, False, True, False, True, False, True, False, False, True],
         [True, True, True, False, True, True, True, True, True, True]],9,1, 0, 6)
