from Specification import *
import Food


class Monster:
    ################################################## CORE FUNCTIONS ##################################################
    def __init__(self, app, pos, cell=None):
        self.app = app
        self.grid_pos = [pos[0], pos[1]]
        self.pixel_pos = self.get_current_pixel_pos()
        self.color = RED
        self.size = CELL_SIZE
        self.ghost1_left = pygame.image.load(GHOST_1_LEFT)
        self.ghost1_left = pygame.transform.scale(self.ghost1_left, (20, 15))

        self.ghost1_right = pygame.image.load(GHOST_1_RIGHT)
        self.ghost1_right = pygame.transform.scale(self.ghost1_right, (20, 15))

        self.ghost2_left = pygame.image.load(GHOST_2_LEFT)
        self.ghost2_left = pygame.transform.scale(self.ghost2_left, (20, 15))

        self.ghost2_right = pygame.image.load(GHOST_2_RIGHT)
        self.ghost2_right = pygame.transform.scale(self.ghost2_right, (20, 15))

        self.black_background = pygame.image.load(BLACK_BG)
        self.black_background = pygame.transform.scale(self.black_background, (20, 20))

        self.count = 0

        self.initial_cell = cell
        self.cell = cell


    def appear(self):
        """
        Make the Monster appear on the screen.
        """
        self.app.screen.blit(self.ghost1_right, (self.pixel_pos[0], self.pixel_pos[1]))


    def move(self, new_grid_pos):
        """
        Move the Monster to the new position (x, y) on the grid map.

        :param new_grid_pos: new position (x, y) on the grid map
        """
        self.draw(self.ghost1_left, self.ghost1_right)
        self.update(new_grid_pos)


    def get_around_cells_of_initial_cell(self, graph_map):
        return graph_map[self.initial_cell]


    def get_around_cells(self, graph_map):
        return graph_map[self.cell]

    ####################################################################################################################

    def update(self, new_grid_pos):
        """
        Update the Monster's grid position

        :param new_grid_pos: new position (x, y) on the grid map
        """
        self.app.screen.blit(self.black_background, (self.pixel_pos[0], self.pixel_pos[1]))
        self.grid_pos = new_grid_pos
        self.pixel_pos = self.get_current_pixel_pos()


    def get_current_pixel_pos(self):
        """
        Get the current pixel position via the current grid position.

        :return: the pixel position [x, y]
        """
        return [self.grid_pos[0] * CELL_SIZE + MAP_POS_X,
                self.grid_pos[1] * CELL_SIZE + MAP_POS_Y]


    def draw(self, image1, image2):
        """
        Draw the Monster onto the screen.
        """
        if self.count == 0:
            self.app.screen.blit(image1, (self.pixel_pos[0] , self.pixel_pos[1]))
            self.count += 1
        elif self.count == 1:
            self.app.screen.blit(image2, (self.pixel_pos[0], self.pixel_pos[1]))
            self.count += -1
        pygame.display.update()



