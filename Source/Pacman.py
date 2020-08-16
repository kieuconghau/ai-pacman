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

        # Pacman's brain
        self.food_cell_in_brain_list = []
        self.path_to_food_cell_in_brain_list = []

        # Pacman's sight
        self.food_cell_in_sight_list = []
        self.monster_cell_in_sight_list = []


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


    def observe(self, graph_map, sight):
        """
        Check if Pacman see nothing in its sight and add all Food_Cells which are in sight of Pacman to its brain.

        :param graph_map: Adjacency list of the map.
        :param sight: The sight of Pacman (sight = 3)
        :return:
        """
        # Reset Pacman's sight.
        self.food_cell_in_sight_list = []
        self.monster_cell_in_sight_list = []

        # Update Pacman's current sight.
        for neighbor_cell in graph_map[self.cell]:
            self.recursive_observe(graph_map, self.cell, neighbor_cell, sight - 1)

        nearby_monster_food_cell_list = []
        for food_cell_in_sight in self.food_cell_in_sight_list:
            if self.nearby_monster_cell(food_cell_in_sight):
                nearby_monster_food_cell_list.append(food_cell_in_sight)

        food_cell_index = []
        for index in range(len(self.food_cell_in_brain_list)):
            if self.nearby_monster_cell(self.food_cell_in_brain_list[index]):
                food_cell_index.append(index)
        if len(food_cell_index) != 0:
            for index in reversed(food_cell_index):
                self.food_cell_in_brain_list.pop(index)
                self.path_to_food_cell_in_brain_list.pop(index)

        for nearby_monster_food_cell in nearby_monster_food_cell_list:
            self.food_cell_in_sight_list.remove(nearby_monster_food_cell)

        # Update Pacman's brain.
        for food_cell_in_sight in self.food_cell_in_sight_list:
            for index in range(len(self.food_cell_in_brain_list)):
                if food_cell_in_sight == self.food_cell_in_brain_list[index]:
                    self.food_cell_in_brain_list.remove(self.food_cell_in_brain_list[index])
                    self.path_to_food_cell_in_brain_list.remove(self.path_to_food_cell_in_brain_list[index])
                    break
            self.food_cell_in_brain_list.append(food_cell_in_sight)
            self.path_to_food_cell_in_brain_list.append([])


    def nearby_monster_cell(self, food_cell):
        for monster_cell in self.monster_cell_in_sight_list:
            if abs(monster_cell.pos[0] - food_cell.pos[0]) + abs(monster_cell.pos[1] - food_cell.pos[1]) <= 2:
                return True

        return False


    def empty_brain(self):
        return len(self.food_cell_in_brain_list) == 0


    def have_monster_in_cur_sight(self):
        return len(self.monster_cell_in_sight_list) != 0


    def have_food_in_cur_sight(self):
        return len(self.food_cell_in_sight_list) != 0


    def spread_peas(self, pacman_old_cell):
        for path_to_food_cell in self.path_to_food_cell_in_brain_list:
            path_to_food_cell.append(pacman_old_cell)


    def back_track(self, graph_map):
        next_cell = self.path_to_food_cell_in_brain_list[-1][-1]

        for path_to_food_cell in self.path_to_food_cell_in_brain_list:
            path_to_food_cell.pop(-1)

        return next_cell


    ####################################################################################################################


    def recursive_observe(self, graph_map, parent_cell, cur_cell, sight):
        if sight >= 0:
            if cur_cell.exist_food() and cur_cell not in self.food_cell_in_sight_list:
                self.food_cell_in_sight_list.append(cur_cell)

            if cur_cell.exist_monster() and cur_cell not in self.monster_cell_in_sight_list:
                self.monster_cell_in_sight_list.append(cur_cell)

            for neighbor_cell in graph_map[cur_cell]:
                if neighbor_cell != parent_cell:
                    self.recursive_observe(graph_map, cur_cell, neighbor_cell, sight - 1)


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
