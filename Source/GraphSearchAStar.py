import queue
import enum
from collections import deque


class V(enum.Enum):
    NOT_VISITED = 0     # state is not visited yet
    FRONTIER = 1        # state is in frontier
    EXPLORED = 2        # state is explored already


def search(graph, start, goal):
    visited = dict()
    for state in graph:
        visited[state] = V.NOT_VISITED

    node = (heuristic(start, goal), start, None)     # node = (path cost, state, parent's state)
    frontier = queue.PriorityQueue()
    explored = []

    frontier.put(node)
    visited[node[1]] = V.FRONTIER

    while frontier.queue:
        node = frontier.get()
        explored.append((node[1], node[2]))
        visited[node[1]] = V.EXPLORED

        if node[1] == goal:
            return get_path(explored)    # success

        for child_state in graph[node[1]]:
            h_state = heuristic(node[1], goal)
            h_child_state = heuristic(child_state, goal)

            if visited[child_state] == V.NOT_VISITED:
                frontier.put((node[0] - h_state + 1 + h_child_state, child_state, node[1]))
                visited[child_state] = V.FRONTIER
            elif visited[child_state] == V.FRONTIER:
                update(frontier, (node[0] - h_state + 1 + h_child_state, child_state, node[1]))

    return None     # failure


def get_path(explored):
    parent_table = dict()
    for node in explored:
        parent_table[node[0]] = node[1]

    state, parent_state = explored[-1][0], explored[-1][1]
    path = deque([state])
    while parent_state is not None:
        state = parent_state
        parent_state = parent_table[state]
        path.appendleft(state)

    return list(path)


def update(frontier, node):
    temp_frontier = []
    while frontier.queue:
        temp_frontier.append(frontier.get())

    for temp_node in temp_frontier:
        if temp_node[1] == node[1]:
            if temp_node[0] > node[0]:
                temp_node = node
        frontier.put(temp_node)


def heuristic(state, goal):      # Manhattan
    return int(abs(state[0] - goal[0]) + abs(state[1] - goal[1]))
