from Specification import *


class Pacman:
    ################################################## CORE FUNCTIONS ##################################################
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = [pos[0], pos[1]]
        self.pixel_pos = self.get_current_pixel_pos()
        self.color = YELLOW
        self.radius = CELL_SIZE // 2 - 1
        self.open_mouth_up = pygame.image.load(OM_UP)
        self.open_mouth_up = pygame.transform.scale(self.open_mouth_up, (20, 20))
        self.open_mouth_down = pygame.image.load(OM_DOWN)
        self.open_mouth_down = pygame.transform.scale(self.open_mouth_down, (20, 20))
        self.open_mouth_left = pygame.image.load(OM_LEFT)
        self.open_mouth_left = pygame.transform.scale(self.open_mouth_left, (20, 20))
        self.open_mouth_right = pygame.image.load(OM_RIGHT)
        self.open_mouth_right = pygame.transform.scale(self.open_mouth_right, (20, 20))
        self.close_mouth_up = pygame.image.load(CM_UP)
        self.close_mouth_up = pygame.transform.scale(self.close_mouth_up, (20, 20))
        self.close_mouth_down = pygame.image.load(CM_DOWN)
        self.close_mouth_down = pygame.transform.scale(self.close_mouth_down, (20, 20))
        self.close_mouth_left = pygame.image.load(CM_LEFT)
        self.close_mouth_left = pygame.transform.scale(self.close_mouth_left, (20, 20))
        self.close_mouth_right = pygame.image.load(CM_RIGHT)
        self.close_mouth_right = pygame.transform.scale(self.close_mouth_right, (20, 20))
        self.black_background = pygame.image.load(BLACK_BG)
        self.black_background = pygame.transform.scale(self.black_background, (20, 20))
        self.count = 0

    def appear(self):
        """
        Make the Pacman appear on the screen.
        """
        self.app.screen.blit(self.open_mouth_right, (self.pixel_pos[0] - 10, self.pixel_pos[1] - 10))
        pygame.display.update()


    def move(self, new_grid_pos):
        """
        Move the Pacman to the new position (x, y) on the grid map.

        :param new_grid_pos: new position (x, y) on the grid map
        """
        if new_grid_pos[1] - self.grid_pos[1] == -1:
            self.draw(self.open_mouth_up, self.close_mouth_up)
        elif new_grid_pos[1] - self.grid_pos[1] == 1:
            self.draw(self.open_mouth_down, self.close_mouth_down)
        elif new_grid_pos[0] - self.grid_pos[0] == 1:
            self.draw(self.open_mouth_right, self.close_mouth_right)
        elif new_grid_pos[0] - self.grid_pos[0] == -1:
            self.draw(self.open_mouth_left, self.close_mouth_left)
        self.update(new_grid_pos)



    ####################################################################################################################


    def update(self, new_grid_pos):
        """
        Update the Pacman's grid position

        :param new_grid_pos: new position (x, y) on the grid map
        """
        self.app.screen.blit(self.black_background, (self.pixel_pos[0] - 10, self.pixel_pos[1] - 10))
        self.grid_pos = new_grid_pos
        self.pixel_pos = self.get_current_pixel_pos()


    def get_current_pixel_pos(self):
        """
        Get the current pixel position via the current grid position.

        :return: the pixel position [x, y]
        """
        return [self.grid_pos[0] * CELL_SIZE + CELL_SIZE // 2 + MAP_POS_X,
                self.grid_pos[1] * CELL_SIZE + CELL_SIZE // 2 + MAP_POS_Y]

    def draw(self, image1, image2):
        """
        Draw the Pacman with the color `color`

        :param color: the color of the Pacman
        """
        if self.count == 0:
            self.app.screen.blit(image1,(self.pixel_pos[0]-10,self.pixel_pos[1]-10))
            self.count += 1
        elif self.count == 1:
            self.app.screen.blit(image2, (self.pixel_pos[0] - 10, self.pixel_pos[1] - 10))
            self.count += -1
        pygame.display.update()
