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
