from HeuristicLocalSearch import *

def input_raw(map_input_path):
    try:
        f = open(map_input_path, "r")
    except:
        print("Can not read file \'" + map_input_path + "\'. Please check again!")
        return None

    pacman_pos = [int(x) for x in next(f).split()]
    raw_map = [[int(num) for num in line if num != '\n'] for line in f]

    return (pacman_pos[0], pacman_pos[1]), raw_map


def read_map_level_1(map_input_path):
    pacman_pos, raw_map = input_raw(map_input_path)
    food_pos = None

    graph_map = {}
    for y in range(len(raw_map)):
        for x in range(len(raw_map[y])):
            if raw_map[y][x] != 1:
                if raw_map[y][x] == 2:
                    food_pos = (x, y)

                cur = (x, y)
                graph_map[cur] = []

                if x - 1 >= 0 and raw_map[y][x - 1] != 1:
                    left = (x - 1, y)
                    graph_map[left] = graph_map[left] + [cur]
                    graph_map[cur] = graph_map[cur] + [left]

                if y - 1 >= 0 and raw_map[y - 1][x] != 1:
                    up = (x, y - 1)
                    graph_map[up] = graph_map[up] + [cur]
                    graph_map[cur] = graph_map[cur] + [up]

    return graph_map, pacman_pos, food_pos


def read_map_level_2(map_input_path, monster_as_wall: bool):
    pacman_pos, raw_map = input_raw(map_input_path)
    food_pos = None
    monster_pos_list = []

    graph_map = {}
    for y in range(len(raw_map)):
        for x in range(len(raw_map[y])):
            if raw_map[y][x] != 1:
                if raw_map[y][x] == 2:
                    food_pos = (x, y)
                elif raw_map[y][x] == 3:
                    monster_pos_list.append((x, y))
                    if monster_as_wall:
                        raw_map[y][x] = 1

                cur = (x, y)
                graph_map[cur] = []

                if x - 1 >= 0 and raw_map[y][x - 1] != 1:
                    left = (x - 1, y)
                    graph_map[left] = graph_map[left] + [cur]
                    graph_map[cur] = graph_map[cur] + [left]

                if y - 1 >= 0 and raw_map[y - 1][x] != 1:
                    up = (x, y - 1)
                    graph_map[up] = graph_map[up] + [cur]
                    graph_map[cur] = graph_map[cur] + [up]

    return graph_map, pacman_pos, food_pos, monster_pos_list

def init_cells(raw_map, pacman_pos):
    cells = []

    for y in range(len(raw_map)):
        row = []
        for x in range(len(raw_map[y])):
            if raw_map[y][x] != 1:
                if raw_map[y][x] == 0:
                    row.append(Cell((x, y), []))
                else:
                    row.append(Cell((x, y), [cState(raw_map[y][x])]))

                if pacman_pos == (x, y):
                    row[x].state.append(cState(4))
                    pacman_cell = row[x]
            else:
                row.append(None)
        cells.append(row)

    return cells, pacman_cell

def read_map_level_3(map_input_path):
    pacman_pos, raw_map = input_raw(map_input_path)

    cells, pacman_cell = init_cells(raw_map, pacman_pos)

    food_cell_list = []
    monster_cell_list = []
    graph_map = {}

    for y in range(len(raw_map)):
        for x in range(len(raw_map[y])):
            if raw_map[y][x] != 1:
                cur = cells[y][x]

                if cState.MONSTER in cur.state:
                    monster_cell_list.append(cur)
                elif cState.FOOD in cur.state:
                    food_cell_list.append(cur)

                graph_map[cur] = []

                if x - 1 >= 0 and raw_map[y][x - 1] != 1:
                    left = cells[y][x - 1]
                    graph_map[left] = graph_map[left] + [cur]
                    graph_map[cur] = graph_map[cur] + [left]

                if y - 1 >= 0 and raw_map[y - 1][x] != 1:
                    up = cells[y - 1][x]
                    graph_map[up] = graph_map[up] + [cur]
                    graph_map[cur] = graph_map[cur] + [up]

    return cells, graph_map, pacman_cell, food_cell_list, monster_cell_list


def read_map_level_4(map_input_path):
    pacman_pos, raw_map = input_raw(map_input_path)

    cells, pacman_cell = init_cells(raw_map, pacman_pos)

    food_cell_list = []
    monster_cell_list = []
    graph_cell = {}
    graph_map = {}

    for y in range(len(raw_map)):
        for x in range(len(raw_map[y])):
            if raw_map[y][x] != 1:
                c_cur = cells[y][x]
                cur = (x, y)

                if cState.MONSTER in cur.state:
                    monster_cell_list.append(c_cur)
                elif cState.FOOD in cur.state:
                    food_cell_list.append(c_cur)

                graph_cell[c_cur] = []
                graph_map[cur] = []

                if x - 1 >= 0 and raw_map[y][x - 1] != 1:
                    c_left = cells[y][x - 1]
                    graph_cell[c_left] = graph_cell[c_left] + [c_cur]
                    graph_cell[c_cur] = graph_cell[c_cur] + [c_left]

                    left = (x - 1, y)
                    graph_map[left] = graph_map[left] + [cur]
                    graph_map[cur] = graph_map[cur] + [left]

                if y - 1 >= 0 and raw_map[y - 1][x] != 1:
                    c_up = cells[y - 1][x]
                    graph_cell[c_up] = graph_cell[c_up] + [c_cur]
                    graph_cell[c_cur] = graph_cell[c_cur] + [c_up]

                    up = (x, y - 1)
                    graph_map[up] = graph_map[up] + [cur]
                    graph_map[cur] = graph_map[cur] + [up]

    return cells, graph_cell, pacman_cell, graph_map, food_cell_list, monster_cell_list
