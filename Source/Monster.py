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

        self.initial_cell = cell
        self.cell = cell


    def appear(self):
        """
        Make the Monster appear on the screen.
        """
        self.draw(self.color)


    def move(self, new_grid_pos):
        """
        Move the Monster to the new position (x, y) on the grid map.

        :param new_grid_pos: new position (x, y) on the grid map
        """
        self.update(new_grid_pos)
        self.draw(self.color)


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
        self.draw(BLACK)
        self.grid_pos = new_grid_pos
        self.pixel_pos = self.get_current_pixel_pos()


    def get_current_pixel_pos(self):
        """
        Get the current pixel position via the current grid position.

        :return: the pixel position [x, y]
        """
        return [self.grid_pos[0] * CELL_SIZE + MAP_POS_X,
                self.grid_pos[1] * CELL_SIZE + MAP_POS_Y]


    def draw(self, color):
        """
        Draw the Monster onto the screen.
        """
        food_rect = pygame.draw.rect(self.app.screen, color,
                                     pygame.Rect(self.pixel_pos[0], self.pixel_pos[1], self.size, self.size))
        pygame.display.update(food_rect)
