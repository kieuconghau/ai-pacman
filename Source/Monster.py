from Specification import *


class Monster:
    ################################################## CORE FUNCTIONS ##################################################
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = [pos[0], pos[1]]
        self.pixel_pos = self.get_current_pixel_pos()
        self.color = RED
        self.size = CELL_SIZE

    def appear(self):
        """
        Make the Monster appear on the screen.
        """
        self.draw()
    ####################################################################################################################


    def get_current_pixel_pos(self):
        """
        Get the current pixel position via the current grid position.

        :return: the pixel position [x, y]
        """
        return [self.grid_pos[0] * CELL_SIZE + MAP_POS_X,
                self.grid_pos[1] * CELL_SIZE + MAP_POS_Y]


    def draw(self):
        """
        Draw the Monster onto the screen.
        """
        food_rect = pygame.draw.rect(self.app.screen, self.color,
                                     pygame.Rect(self.pixel_pos[0], self.pixel_pos[1], self.size, self.size))
        pygame.display.update(food_rect)
