from Specification import *


class Pacman:
    ################################################## CORE FUNCTIONS ##################################################
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = [pos[0], pos[1]]
        self.pixel_pos = self.get_current_pixel_pos()
        self.color = YELLOW
        self.radius = CELL_SIZE // 2 - 1

    def appear(self):
        """
        Make the Pacman appear on the screen.
        """
        self.draw(self.color)
        pygame.display.update()


    def move(self, new_grid_pos):
        """
        Move the Pacman to the new position (x, y) on the grid map.

        :param new_grid_pos: new position (x, y) on the grid map
        """
        self.update(new_grid_pos)
        self.pixel_pos = self.get_current_pixel_pos()
        self.draw(self.color)
        pygame.display.update()
    ####################################################################################################################


    def update(self, new_grid_pos):
        """
        Update the Pacman's grid position

        :param new_grid_pos: new position (x, y) on the grid map
        """
        self.draw(BLACK)
        self.grid_pos = new_grid_pos


    def get_current_pixel_pos(self):
        """
        Get the current pixel position via the current grid position.

        :return: the pixel position [x, y]
        """
        return [self.grid_pos[0] * CELL_SIZE + CELL_SIZE // 2 + MAP_POS_X,
                self.grid_pos[1] * CELL_SIZE + CELL_SIZE // 2 + MAP_POS_Y]


    def draw(self, color):
        """
        Draw the Pacman with the color `color`

        :param color: the color of the Pacman
        """
        pygame.draw.circle(self.app.screen, color, self.pixel_pos, self.radius)
