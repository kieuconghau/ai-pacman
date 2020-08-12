import pygame
import sys
import os
import pygame.freetype
from Specification import *


class MyApp:
    #constructor
    def __init__(self):
        pygame.init()
        self.fontdir = os.path.dirname(os.path.abspath(__file__))
        self.font = pygame.freetype.Font(os.path.join(self.fontdir, "Fonts", initFont))
        self.screen = pygame.display.set_mode((Width, Height))
        self.caption = pygame.display.set_caption('Pacman')
        self.background = pygame.image.load('bg.png')
        self.background = pygame.transform.scale(self.background, (Width-50, Height-410))
        self.playbackground = pygame.image.load('maze.png')
        self.playbackground = pygame.transform.scale(self.playbackground, (Width - 50, Height - 60))
        self.aboutbackground = pygame.image.load('background.png')
        self.aboutbackground = pygame.transform.scale(self.aboutbackground, (Width, Height))
        self.mapOne = pygame.image.load('maze.png')
        self.m = pygame.image.load('map.png')
        self.map = 1
        self.state = 'init'
        self.isRunning = True
        self.difficult = level
        self.clock = pygame.time.Clock()
    def drawButton(self, surf, rect, buttonColor, text_color, text):
        pygame.draw.rect(surf, buttonColor, rect)
        text_surf, text_rect = self.font.render(text, text_color)
        text_rect.center = rect.center
        self.screen.blit(text_surf, text_rect)
    def drawTriangleButton(self, surf, rect, buttonColor):
        pygame.draw.polygon(surf, buttonColor, rect)
    def initDraw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (50//2, 50//2))
    def playDraw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.playbackground, (50 // 2, 50 // 2))
    def aboutDraw(self):
        self.screen.fill(BLACK)
        self.caption = pygame.display.set_caption('About')
        self.screen.blit(self.aboutbackground, (0, 0))
        text_surf, text_rect = self.font.render("PROGRAMMERS", TOMATO)
        self.screen.blit(text_surf, (240,100))
        text_surf, text_rect = self.font.render("18127017 - Nguyen Hoang Nhan", TOMATO)
        self.screen.blit(text_surf, (150, 150))
        text_surf, text_rect = self.font.render("18127259 - Kieu Cong Hau", TOMATO)
        self.screen.blit(text_surf, (150, 200))
        text_surf, text_rect = self.font.render("18127267 - Tran Dinh Sang", TOMATO)
        self.screen.blit(text_surf, (150, 250))
        text_surf, text_rect = self.font.render("18127268 - Tran Thanh Tam", TOMATO)
        self.screen.blit(text_surf, (150, 300))
    def levelDraw(self):
        self.levelbackground = self.background
        self.screen.fill(BLACK)
        self.screen.blit(self.levelbackground, (50 // 2, 50 // 2))
    def settingDraw(self):
        self.screen.fill(BLACK)

    def settingEvent(self):
        if self.map == 1:
            self.mapOne = pygame.transform.scale(self.mapOne, (Width - 50, Height - 64))
            self.screen.blit(self.mapOne, (50 // 2, 0 // 2))
        elif self.map == 2:
            self.m = pygame.transform.scale(self.m, (Width - 50, Height - 64))
            self.screen.blit(self.m, (50 // 2, 0 // 2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 255 <= self.mouse[0] <= 355 and 620 <= self.mouse[1] <= 670:
                    self.state = 'init'
                elif 360 <= self.mouse[0] <= 403.3 and 620 <= self.mouse[1] <= 670:
                    if self.map < 2:
                        self.map += 1
                elif 206.7 <= self.mouse[0] <= 250 and 620 <= self.mouse[1] <= 670:
                    if self.map > 1:
                        self.map -=1
        self.mouse = pygame.mouse.get_pos()
        if 255 <= self.mouse[0] <= 355 and 620 <= self.mouse[1] <= 670:
            self.drawButton(self.screen, okPos, DarkColor, RED, "OK")
        else:
            self.drawButton(self.screen, okPos, LightColor, BLACK, "OK")
        if 360 <= self.mouse[0] <= 403.3 and 620 <= self.mouse[1] <= 670:
            self.drawTriangleButton(self.screen, triangle1Pos, DarkColor)
        else:
            self.drawTriangleButton(self.screen, triangle1Pos, LightColor)
        if 206.7 <= self.mouse[0] <= 250 and 620 <= self.mouse[1] <= 670:
            self.drawTriangleButton(self.screen, triangle2Pos, DarkColor)
        else:
            self.drawTriangleButton(self.screen, triangle2Pos, LightColor)
        pygame.display.update()
    def playEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False
        pygame.display.update()
    def aboutEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 400 <= self.mouse[0] <= 600 and 560 <= self.mouse[1] <= 610:
                    self.state = 'init'
        self.mouse = pygame.mouse.get_pos()
        if 400 <= self.mouse[0] <= 600 and 560 <= self.mouse[1] <= 610:
            self.drawButton(self.screen, backPos, DarkColor, RED, "Back")
        else:
            self.drawButton(self.screen, backPos, LightColor, BLACK, "Back")
        pygame.display.update()
    def levelEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 150 <= self.mouse[0] <= 450 and 320 <= self.mouse[1] <= 395:
                    self.state = 'playing'
                    self.difficult = 1
                elif 150 <= self.mouse[0] <= 450 and 400 <= self.mouse[1] <= 450:
                    self.state = 'playing'
                    self.difficult = 2
                elif 150 <= self.mouse[0] <= 450 and 480 <= self.mouse[1] <= 530:
                    self.state = 'playing'
                    self.difficult = 3
                elif 150 <= self.mouse[0] <= 450 and 560 <= self.mouse[1] <= 610:
                    self.state = 'playing'
                    self.difficult = 4
                elif 150 <= self.mouse[0] <= 450 and 600 <= self.mouse[1] <= 900:
                    self.state = 'init'
            elif event.type == pygame.QUIT:
                self.isRunning = False
        self.mouse = pygame.mouse.get_pos()
        if 150 <= self.mouse[0] <= 450 and 320 <= self.mouse[1] <= 375:
            self.drawButton(self.screen, levelOnePos, DarkColor, RED, "Level 1")
        else:
            self.drawButton(self.screen, levelOnePos, LightColor, BLACK, "Level 1")
        if 150 <= self.mouse[0] <= 450 and 400 <= self.mouse[1] <= 450:
            self.drawButton(self.screen, levelTwoPos, DarkColor, RED, "Level 2")
        else:
            self.drawButton(self.screen, levelTwoPos, LightColor, BLACK, "Level 2")
        if 150 <= self.mouse[0] <= 450 and 480 <= self.mouse[1] <= 530:
            self.drawButton(self.screen, levelThreePos, DarkColor, RED, "Level 3")
        else:
            self.drawButton(self.screen, levelThreePos, LightColor, BLACK, "Level 3")
        if 150 <= self.mouse[0] <= 450 and 560 <= self.mouse[1] <= 610:
            self.drawButton(self.screen, levelFourPos, DarkColor, RED, "Level 4")
        else:
            self.drawButton(self.screen, levelFourPos, LightColor, BLACK, "Level 4")
        if 150 <= self.mouse[0] <= 450 and 600 <= self.mouse[1] <= 900:
            self.drawButton(self.screen, backLevelPos, DarkColor, RED, "Back")
        else:
            self.drawButton(self.screen, backLevelPos, LightColor, BLACK, "Back")
        pygame.display.update()
    def initEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 150 <= self.mouse[0] <= 450 and 320 <= self.mouse[1] <= 395:
                    self.state = 'level'
                elif 150 <= self.mouse[0] <= 450 and 400 <= self.mouse[1] <= 450:
                    self.state = 'setting'
                elif 150 <= self.mouse[0] <= 450 and 480 <= self.mouse[1] <= 530:
                    self.state = 'about'
                elif 150 <= self.mouse[0] <= 450 and 560 <= self.mouse[1] <= 610:
                    self.isRunning = False
            elif event.type == pygame.QUIT:
                self.isRunning = False
        self.mouse = pygame.mouse.get_pos()
        if 150 <= self.mouse[0] <= 450 and 320 <= self.mouse[1] <= 375:
            self.drawButton(self.screen, startPos, DarkColor, RED, "Start")
        else:
            self.drawButton(self.screen, startPos, LightColor, BLACK, "Start")
        if 150 <= self.mouse[0] <= 450 and 400 <= self.mouse[1] <= 450:
            self.drawButton(self.screen, levelPos, DarkColor, RED, "Setting")
        else:
            self.drawButton(self.screen, levelPos, LightColor, BLACK, "Setting")
        if 150 <= self.mouse[0] <= 450 and 480 <= self.mouse[1] <= 530:
            self.drawButton(self.screen, aboutPos, DarkColor, RED, "About")
        else:
            self.drawButton(self.screen, aboutPos, LightColor, BLACK, "About")
        if 150 <= self.mouse[0] <= 450 and 560 <= self.mouse[1] <= 610:
            self.drawButton(self.screen, quitPos, DarkColor, RED, "Exit")
        else:
            self.drawButton(self.screen, quitPos, LightColor, BLACK, "Exit")
        pygame.display.update()
    def run(self):
        while self.isRunning:
            if self.state == 'init':
                self.initDraw()
                self.initEvent()
            elif self.state == 'playing':
                self.playDraw()
                self.playEvent()
            elif self.state == 'about':
                self.aboutDraw()
                self.aboutEvent()
            elif self.state == 'level':
                self.levelDraw()
                self.levelEvent()
            elif self.state == 'setting':
                self.settingDraw()
                self.settingEvent()
            else:
                self.isRunning = False
        self.clock.tick(60)
        pygame.quit()
        sys.exit()

a = MyApp()
a.run()
