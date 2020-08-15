from Specification import *


class Food:
    ################################################## CORE FUNCTIONS ##################################################
    def __init__(self, app, pos, cell=None):
        self.app = app
        self.width = 10
        self.grid_pos = [pos[0], pos[1]]
        self.pixel_pos = self.get_current_pixel_pos()

        self.image = pygame.image.load(FOOD_IMAGE)
        self.image = pygame.transform.scale(self.image, (self.width, self.width))

        self.cell = cell

    def appear(self):
        """
        Make the Food appear on the screen.
        """
        self.draw()


    def get_pos(self):
        return self.grid_pos[0], self.grid_pos[1]

    ####################################################################################################################


    def get_current_pixel_pos(self):
        """
        Get the current pixel position via the current grid position.

        :return: the pixel position [x, y]
        """
        return [self.grid_pos[0] * CELL_SIZE + CELL_SIZE // 2 - self.width // 2 + MAP_POS_X,
                self.grid_pos[1] * CELL_SIZE + CELL_SIZE // 2 - self.width // 2 + MAP_POS_Y]


    def draw(self):
        """
        Draw the Food onto the screen.
        """
        food_rect = self.app.screen.blit(self.image, (self.pixel_pos[0], self.pixel_pos[1]))
        pygame.display.update(food_rect)
