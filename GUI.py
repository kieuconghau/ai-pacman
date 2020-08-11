import pygame
import sys
import os
import pygame.freetype
from Specification import *


class GUI:
    #constructor
    def __init__(self):
        pygame.init()
        self.fontdir = os.path.dirname(os.path.abspath(__file__))
        self.font = pygame.freetype.Font(os.path.join(self.fontdir, "Fonts", initFont))
        self.screen = pygame.display.set_mode((Width, Height))
        self.caption = pygame.display.set_caption('Pacman')
        self.background = pygame.image.load('bg.png')
        self.background = pygame.transform.scale(self.background, (Width-50, Height-400))
        self.playbackground = pygame.image.load('maze.png')
        self.playbackground = pygame.transform.scale(self.playbackground, (Width - 50, Height - 50))
        self.state = 'init'
        self.isRunning = True
        self.clock = pygame.time.Clock()
    def drawButton(self, surf, rect, buttonColor, text_color, text):
        pygame.draw.rect(surf, buttonColor, rect)
        text_surf, text_rect = self.font.render(text, text_color)
        text_rect.center = rect.center
        self.screen.blit(text_surf, text_rect)
    def initDraw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (50//2, 50//2))
    def playDraw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.playbackground, (50 // 2, 50 // 2))
        pygame.display.update()
    def aboutDraw(self):
        self.screen.fill(BLACK)
        #self.screen.blit(self.playbackground, (50 // 2, 50 // 2))
        pygame.display.update()
    def playEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False
    def aboutEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False
    def getInitEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 150 <= self.mouse[0] <= 450 and 320 <= self.mouse[1] <= 395:
                    self.state = 'playing'
                elif 150 <= self.mouse[0] <= 450 and 400 <= self.mouse[1] <= 450:
                    self.state = 'about'
                elif 150 <= self.mouse[0] <= 450 and 480 <= self.mouse[1] <= 530:
                    self.isRunning = False
            elif event.type == pygame.QUIT:
                self.isRunning = False
        self.mouse = pygame.mouse.get_pos()
        if 150 <= self.mouse[0] <= 450 and 320 <= self.mouse[1] <= 375:
            self.drawButton(self.screen, startPos, DarkColor, RED, "Start")
        else:
            self.drawButton(self.screen, startPos, LightColor, BLACK, "Start")

        if 150 <= self.mouse[0] <= 450 and 400 <= self.mouse[1] <= 450:
            self.drawButton(self.screen, aboutPos, DarkColor, RED, "About")
        else:
            self.drawButton(self.screen, aboutPos, LightColor, BLACK, "About")

        if 150 <= self.mouse[0] <= 450 and 480 <= self.mouse[1] <= 530:
            self.drawButton(self.screen, quitPos, DarkColor, RED, "Exit")
        else:
            self.drawButton(self.screen, quitPos, LightColor, BLACK, "Exit")
        pygame.display.update()
    def run(self):
        while self.isRunning:
            if self.state == 'init':
                self.initDraw()
                self.getInitEvent()
            elif self.state == 'playing':
                self.playDraw()
                self.playEvent()
            elif self.state == 'about':
                self.aboutDraw()
                self.aboutEvent()
            else:
                self.isRunning = False
        self.clock.tick(60)
        pygame.quit()
        sys.exit()

a = GUI()
a.run()
