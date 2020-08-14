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

        self.visited += 1

    def function(self):
        return self.heuristic - self.visited

def calc_heuristic(cells, graph_map, remembered, start, cur, maxDepth):
    remembered.append(cur.pos)

    if maxDepth <= 0:
        return

    for child in graph_map[cur]:
        if child.pos not in remembered:

            sub_remembered = []
            if child.exist_food():
                update_heuristic(cells, graph_map, sub_remembered, start, child, 2, "food")

            sub_remembered = []
            if child.exist_monster():
                update_heuristic(cells, graph_map, sub_remembered, start, child, 2, "monster")

            calc_heuristic(cells, graph_map, remembered.copy(), start, child, maxDepth - 1)

    cur.heuristic -= cur.visited

def clear_heuristic(cells, graph_map, remembered, cur, maxDepth):
    remembered.append(cur.pos)

    if maxDepth <= 0:
        return

    for child in graph_map[cur]:
        if child.pos not in remembered:
            child.reset_heuristic()

            clear_heuristic(cells, graph_map, remembered.copy(), child, maxDepth - 1)


def update_heuristic(cells, graph_map, remembered, start, cur, maxDepth, type):
    remembered.append(cur.pos)

    if maxDepth < 0:
        return

    if cur.pos == start.pos:
        return

    if type == "food":
        food = 0
        if maxDepth == 2: food = 35
        if maxDepth == 1: food = 10
        if maxDepth == 0: food = 5
        cur.heuristic += food

    if type == "monster":
        monster = 0
        if maxDepth == 2: monster = float("-inf")
        if maxDepth == 1: monster = -100
        if maxDepth == 0: monster = -50
        cur.heuristic += monster


    for child in graph_map[cur]:
        if child.pos not in remembered:
            update_heuristic(cells, graph_map, remembered.copy(), start, child, maxDepth - 1, type)


def local_search(cells, graph_map, pacman_pos):
    remembered = [] 
    clear_heuristic(cells, graph_map, remembered, pacman_pos, 3)

    remembered = []
    calc_heuristic(cells, graph_map, remembered, pacman_pos, pacman_pos, 3)

    max_f = float("-inf")
    next_step = None

    for child in graph_map[pacman_pos]:
        if max_f < child.function():
            max_f = child.function()
            next_step = child

    return next_step
