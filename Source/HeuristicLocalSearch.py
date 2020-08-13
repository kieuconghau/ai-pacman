from enum import Enum

class cState(Enum):
    FOOD = 2
    MONSTER = 3
    PACMAN = 4

class Cell:
    def __init__(self, pos, state):
        self.pos = pos
        self.heuristic = 0
        self.visited = 0
        self.state = state

    def visisted(self):
        self.visited += 1

    def exist_food(self):
        return cState.FOOD in self.state

    def exist_monster(self):
        return cState.MONSTER in self.state

    def reset_heuristic(self):
        self.heuristic = 0

    def food_ate(self):
        self.state.remove(cState.FOOD)

    def monster_leave(self):
        self.state.remove(cState.MONSTER)

    def monster_come(self):
        self.state.append(cState.MONSTER)

    def pacman_leave(self):
        self.state.remove(cState.PACMAN)

    def pacman_come(self):
        self.state.append(cState.PACMAN)

        if cState.FOOD in self.state:
            self.state.remove(cState.FOOD)

def heuristic(cells, graph_map, remembered, cur, maxDepth):
    remembered.append(cur.pos)

    if maxDepth <= 0:
        return

    for child in graph_map(cur):
        if child.pos not in remembered:
            child.reset_heuristic()

            sub_remembered = []

            if child.exist_food():
                update_heuristic(cells, graph_map, sub_remembered, child, 2, "food")

            if child.exist_monster():
                update_heuristic(cells, graph_map, sub_remembered, child, 2, "monster")

            heuristic(cells, graph_map, remembered.copy(), child, maxDepth - 1)

    cur.heuristic -= cur.visited


def update_heuristic(cells, graph_map, remembered, cur, maxDepth, type):
    remembered.append(cur.pos)
    if maxDepth <= 0:
        return

    if type == "food":
        food = 0
        if maxDepth == 2: food = 15
        if maxDepth == 1: food = 10
        if maxDepth == 0: food = 5
        cur.heuristic += food

    if type == "monster":
        monster = 0
        if maxDepth == 2: monster = float("-inf")
        if maxDepth == 1: monster = -50
        if maxDepth == 0: monster = -25
        cur.heuristc += monster

    for child in graph_map(cur):
        if child.pos not in remembered:
            update_heuristic(cells, graph_map, remembered.copy(), child, maxDepth - 1, type)


def local_search(cells, graph_map, pacman_pos):
    remembered = []
    heuristic(cells, graph_map, remembered, pacman_pos, 3)

    max = float("-inf")
    next_step = None
    for child in graph_map(pacman_pos):
        if max < child.heuristic:
            max = child.heuristic
            next_step = child

    return child