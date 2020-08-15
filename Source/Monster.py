from Specification import *
import Food


class Monster:
    ################################################## CORE FUNCTIONS ##################################################
    def __init__(self, app, pos, cell=None):
        self.app = app
        self.width = CELL_SIZE - 2
        self.grid_pos = [pos[0], pos[1]]
        self.pixel_pos = self.get_current_pixel_pos()
        self.direction = 'up'

        self.monster_left_image = pygame.image.load(MONSTER_LEFT_IMAGE)
        self.monster_left_image = pygame.transform.scale(self.monster_left_image, (self.width, self.width))
        self.monster_right_image = pygame.image.load(MONSTER_RIGHT_IMAGE)
        self.monster_right_image = pygame.transform.scale(self.monster_right_image, (self.width, self.width))
        self.monster_up_image = pygame.image.load(MONSTER_UP_IMAGE)
        self.monster_up_image = pygame.transform.scale(self.monster_up_image, (self.width, self.width))
        self.monster_down_image = pygame.image.load(MONSTER_DOWN_IMAGE)
        self.monster_down_image = pygame.transform.scale(self.monster_down_image, (self.width, self.width))
        self.black_background = pygame.image.load(BLACK_BG)
        self.black_background = pygame.transform.scale(self.black_background, (CELL_SIZE, CELL_SIZE))
        self.initial_cell = cell
        self.cell = cell


    def appear(self):
        """
        Make the Monster appear on the screen.
        """
        self.draw()


    def move(self, new_grid_pos):
        """
        Move the Monster to the new position (x, y) on the grid map.

        :param new_grid_pos: new position (x, y) on the grid map
        """
        self.update(new_grid_pos)
        self.draw()


    def get_around_cells_of_initial_cell(self, graph_map):
        return graph_map[self.initial_cell]


    def get_around_cells(self, graph_map):
        return graph_map[self.cell]

    ####################################################################################################################

    def update_direction(self, new_grid_pos):
        """
        Update the Monster's direction based on the `new_grid_pos`.
        
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
        Update the Monster's grid position

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
        Draw the Monster onto the screen.
        """
        if self.direction == 'up':
            pygame.display.update(self.app.screen.blit(self.monster_up_image, (self.pixel_pos[0], self.pixel_pos[1])))
        elif self.direction == 'down':
            pygame.display.update(self.app.screen.blit(self.monster_down_image, (self.pixel_pos[0], self.pixel_pos[1])))
        elif self.direction == 'left':
            pygame.display.update(self.app.screen.blit(self.monster_left_image, (self.pixel_pos[0], self.pixel_pos[1])))
        elif self.direction == 'right':
            pygame.display.update(self.app.screen.blit(self.monster_right_image, (self.pixel_pos[0], self.pixel_pos[1])))
