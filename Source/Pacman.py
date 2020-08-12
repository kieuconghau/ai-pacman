from Specification import *

class Pacman:
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.pixel_pos = self.get_current_pixel_pos()
        self.color = YELLOW
        self.radius = self.app.cell_size // 2 - 1


    def appear(self):
        self.draw(self.color)


    def update(self, direction):
        self.draw(BLACK)

        if direction == 'left':
            self.grid_pos[0] -= 1
        elif direction == 'right':
            self.grid_pos[0] += 1
        elif direction == 'up':
            self.grid_pos[1] -= 1
        elif direction == 'down':
            self.grid_pos[1] += 1


    def move(self, direction):
        self.update(direction)
        self.pixel_pos = self.get_current_pixel_pos()
        self.draw(self.color)


    def get_current_pixel_pos(self):
        return [self.grid_pos[0] * self.app.cell_size + self.app.cell_size // 2 + MAP_POS_X,
                self.grid_pos[1] * self.app.cell_size + self.app.cell_size // 2 + MAP_POS_Y]


    def draw(self, color):
        pygame.draw.circle(self.app.screen, color, self.pixel_pos, self.radius)