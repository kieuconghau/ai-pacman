import pygame
import sys
from Specification import *


class GUI:
    #constructor
    def __init__(self):
        self.screen = pygame.display.set_mode((Width, Height))
        self.caption = pygame.display.set_caption('Pacman')
        self.state = 'init'
        self.isRunning = True
        self.clock = pygame.time.Clock()
    def initDraw(self):
        self.screen.fill(BG_color)
        pygame.display.flip()
    def getInitEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False
    def run(self):
        while self.isRunning:
            if self.state == 'init':
                self.initDraw()
                self.getInitEvent()
            else:
                self.isRunning = False
        self.clock.tick(60)
        pygame.quit()
        sys.exit()

a = GUI()
a.run()
