from Specification import *


class Pacman:
    ################################################## CORE FUNCTIONS ##################################################
    def __init__(self, app, pos):
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

    ####################################################################################################################


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
