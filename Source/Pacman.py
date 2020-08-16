from Specification import *


class Pacman:
    ################################################## CORE FUNCTIONS ##################################################
    def __init__(self, app, pos, cell=None):
        self.app = app
        self.width = CELL_SIZE
        self.grid_pos = [pos[0], pos[1]]
        self.pixel_pos = self.get_current_pixel_pos()
        self.direction = 'right'
        self.open_mouth_turn = False

        self.pacman_img = pygame.image.load(PACMAN_IMAGE)
        self.pacman_img = pygame.transform.scale(self.pacman_img, (self.width, self.width))
        self.pacman_left_img = pygame.image.load(PACMAN_LEFT)
        self.pacman_left_img = pygame.transform.scale(self.pacman_left_img, (self.width, self.width))
        self.pacman_right_img = pygame.image.load(PACMAN_RIGHT)
        self.pacman_right_img = pygame.transform.scale(self.pacman_right_img, (self.width, self.width))
        self.pacman_down_img = pygame.image.load(PACMAN_DOWN)
        self.pacman_down_img = pygame.transform.scale(self.pacman_down_img, (self.width, self.width))
        self.pacman_up_img = pygame.image.load(PACMAN_UP)
        self.pacman_up_img = pygame.transform.scale(self.pacman_up_img, (self.width, self.width))
        self.black_background = pygame.image.load(BLACK_BG)
        self.black_background = pygame.transform.scale(self.black_background, (self.width, self.width))

        self.cell = cell

        self.food_cell_in_sight_list = []
        self.path_to_food_cell_list = []
        self.cur_food_cell_in_sight_list = []
        self.cur_monster_in_sight_list = []


    def appear(self):
        """
        Make the Pacman appear on the screen.
        """
        self.draw()


    def move(self, new_grid_pos):
        """
        Move the Pacman to the new position (x, y) on the grid map.

        :param new_grid_pos: new position (x, y) on the grid map
        """
        pygame.display.update(self.app.screen.blit(self.pacman_img, (self.pixel_pos[0], self.pixel_pos[1])))
        self.update(new_grid_pos)
        self.draw()


    def see_nothing(self, graph_map, sight):
        """
        Check if Pacman see nothing in its sight and add all Food_Cells which are in sight of Pacman to its brain.

        :param graph_map: Adjacency list of the map.
        :param sight: The sight of Pacman (sight = 3)
        :return:
        """
        self.cur_food_cell_in_sight_list = []
        self.cur_monster_in_sight_list = []

        for neighbor_cell in graph_map[self.cell]:
            self.recursive_see_nothing(graph_map, self.cell, neighbor_cell, sight - 1)

        return len(self.cur_food_cell_in_sight_list) == 0 and len(self.cur_monster_in_sight_list) == 0


    def spread_peas(self, pacman_old_cell):
        for path_to_food_cell in self.path_to_food_cell_list:
            path_to_food_cell.append(pacman_old_cell)


    def backtrack_nearest_food_in_sight(self, graph_map):
        next_cell = self.path_to_food_cell_list[-1][-1]

        print(self.food_cell_in_sight_list[-1].pos, end='')
        print([food.pos for food in self.path_to_food_cell_list[-1]])

        for path_to_food_cell in self.path_to_food_cell_list:
            path_to_food_cell.pop(-1)

        if abs(next_cell.pos[0] - self.grid_pos[0]) + abs(next_cell.pos[1] - self.grid_pos[1]) != 1:
            print("WAIT!")

        return next_cell


    ####################################################################################################################


    def recursive_see_nothing(self, graph_map, parent_cell, cur_cell, sight):
        if sight >= 0:
            if cur_cell.exist_food() and cur_cell not in self.food_cell_in_sight_list:
                self.food_cell_in_sight_list.append(cur_cell)
                self.path_to_food_cell_list.append([])

            if cur_cell.exist_food() and cur_cell not in self.cur_food_cell_in_sight_list:
                self.cur_food_cell_in_sight_list.append(cur_cell)

            if cur_cell.exist_monster() and cur_cell not in self.cur_monster_in_sight_list:
                self.cur_monster_in_sight_list.append(cur_cell)

            for neighbor_cell in graph_map[cur_cell]:
                if neighbor_cell != parent_cell:
                    self.recursive_see_nothing(graph_map, cur_cell, neighbor_cell, sight - 1)


    def update_direction(self, new_grid_pos):
        """
        Update the Pacman's direction based on the `new_grid_pos`.

        :param new_grid_pos: new position (x, y) on the grid map
        """
        if new_grid_pos[0] - self.grid_pos[0] == 1:
            self.direction = 'right'
        elif new_grid_pos[0] - self.grid_pos[0] == -1:
            self.direction = 'left'
        elif new_grid_pos[1] - self.grid_pos[1] == 1:
            self.direction = 'down'
        elif new_grid_pos[1] - self.grid_pos[1] == -1:
            self.direction = 'up'


    def update(self, new_grid_pos):
        """
        Update the Pacman's grid position

        :param new_grid_pos: new position (x, y) on the grid map
        """
        pygame.display.update(self.app.screen.blit(self.black_background, (self.pixel_pos[0], self.pixel_pos[1])))
        self.update_direction(new_grid_pos)
        self.grid_pos = new_grid_pos
        self.pixel_pos = self.get_current_pixel_pos()


    def get_current_pixel_pos(self):
        """
        Get the current pixel position via the current grid position.

        :return: the pixel position [x, y]
        """
        return [self.grid_pos[0] * CELL_SIZE + CELL_SIZE // 2 - self.width // 2 + MAP_POS_X,
                self.grid_pos[1] * CELL_SIZE + CELL_SIZE // 2 - self.width // 2 + MAP_POS_Y]


    def draw(self):
        """
        Draw the Pacman with the color `color`
        """

        if self.open_mouth_turn:
            self.open_mouth_turn = False
            if self.direction == 'up':
                pygame.display.update(self.app.screen.blit(self.pacman_up_img, (self.pixel_pos[0], self.pixel_pos[1])))
            elif self.direction == 'down':
                pygame.display.update(
                    self.app.screen.blit(self.pacman_down_img, (self.pixel_pos[0], self.pixel_pos[1])))
            elif self.direction == 'left':
                pygame.display.update(
                    self.app.screen.blit(self.pacman_left_img, (self.pixel_pos[0], self.pixel_pos[1])))
            elif self.direction == 'right':
                pygame.display.update(
                    self.app.screen.blit(self.pacman_right_img, (self.pixel_pos[0], self.pixel_pos[1])))
        else:
            self.open_mouth_turn = True
            pygame.display.update(self.app.screen.blit(self.pacman_img, (self.pixel_pos[0], self.pixel_pos[1])))
