from enum import Enum
import os

class pState(Enum):
    EMPTY = 0
    FOOD = 2
    MONSTER = 3
    PACMAN = 4

class Coordinate:
    
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print ((self.x, self.y))

class Path:

    # pos: Coordinate(x,y)
    # state: list containt pState
    
    def __init__(self, pos, state):
        self.pos = pos
        self.state = state
    
    def exMonster(self):
        return pState.MONSTER in self.state

    def exFood(self):
        return pState.FOOD in self.state

    def exPacman(self):
        return pState.PACMAN in self.state
 
    def isEmpty(self):
        return pState.EMPTY in self.state
    
    def display(self):
        self.pos.display()
        print(self.state)

def inputRaw(path):
    if not os.path.exists(path):
        return False

    f = open(path, "r")

    return [[int(num) for num in line if num != '\n'] for line in f] 
        
def initMaze(raw):
    path = []
    for y in range(len(raw)):
        row = []

        for x in range(len(raw[y])):
            if raw[y][x] != 1:
                row.append(Path(pos = Coordinate(x,y), state = [pState(raw[y][x])]))
            else:
                row.append(None)
        
        path.append(row)

    maze = {}
    for y in range(len(raw)):
        for x in range(len(raw[y])):
            if raw[y][x] != 1:
                cur = path[y][x]
                maze[cur] = []

                if x - 1 >= 0 and raw[y][x - 1] != 1:
                    left = path[y][x - 1]
                    maze[left] = maze[left] + [cur]
                    maze[cur] = maze[cur] + [left] 

                if y - 1 >= 0 and raw[y - 1][x] != 1:
                    up = path[y - 1][x]
                    maze[up] = maze[up] + [cur]
                    maze[cur] = maze[cur] + [up] 

    return maze

raw = inputRaw("maze.txt")
maze = initMaze(raw)





