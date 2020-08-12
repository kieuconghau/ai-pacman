import sys
import pygame.freetype
from Pacman import *

class MyApp:
    def __init__(self):
        pygame.init()

        self.font = pygame.freetype.Font(INIT_FONT)
        self.screen = pygame.display.set_mode((APP_WIDTH, APP_HEIGHT))
        self.caption = pygame.display.set_caption(APP_CAPTION)

        self.home_background = pygame.image.load(HOME_BACKGROUND)
        self.home_background = pygame.transform.scale(self.home_background, (HOME_BG_WIDTH, HOME_BG_HEIGHT))
        self.play_background = pygame.image.load(MAP_1)
        self.play_background = pygame.transform.scale(self.play_background, (MAP_WIDTH, MAP_HEIGHT))
        self.about_background = pygame.image.load(ABOUT_BACKGROUND)
        self.about_background = pygame.transform.scale(self.about_background, (APP_WIDTH, APP_HEIGHT))
        self.level_background = None

        self.map_1 = pygame.image.load(MAP_1)
        self.map_2 = pygame.image.load(MAP_2)
        self.current_map = 1

        self.state = STATE_HOME
        self.is_running = True
        self.difficult = CURRENT_LEVEL
        self.clock = pygame.time.Clock()
        self.mouse = None

        self.score = 0
        self.cell_size = MAP_WIDTH // 28

        self.pacman = None


    def launch_pacman_game(self):
        self.draw_grids()

        self.pacman = Pacman(self, [1, 1])

        self.pacman.appear()
        pygame.display.update()
        pygame.time.wait(1000)

        dir_list = ['left', 'right', 'up', 'down']
        path = [1, 1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 3, 3]

        for i in range(len(path)):
            self.pacman.move(dir_list[path[i]])
            pygame.display.update()
            pygame.time.wait(500)


    def draw_grids(self):
        for x in range(int(MAP_WIDTH / self.cell_size) + 1):
            pygame.draw.line(self.screen, (107, 107, 107),
                             (x*self.cell_size + MAP_POS_X, MAP_POS_Y),
                             (x * self.cell_size + MAP_POS_X, MAP_HEIGHT + MAP_POS_Y))

        for y in range(int(MAP_HEIGHT / self.cell_size) + 1):
            pygame.draw.line(self.screen, (107, 107, 107),
                             (MAP_POS_X, y*self.cell_size + MAP_POS_Y),
                             (MAP_WIDTH + MAP_POS_X, y * self.cell_size + MAP_POS_Y))


    def draw_button(self, surf, rect, button_color, text_color, text):
        pygame.draw.rect(surf, button_color, rect)
        text_surf, text_rect = self.font.render(text, text_color)
        text_rect.center = rect.center
        self.screen.blit(text_surf, text_rect)


    def draw_triangle_button(self, surf, rect, button_color):
        pygame.draw.polygon(surf, button_color, rect)


    def home_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.home_background, (0, 0))


    def play_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.play_background, (MAP_POS_X, MAP_POS_Y))


    def about_draw(self):
        self.screen.fill(BLACK)
        self.caption = pygame.display.set_caption(STATE_ABOUT)
        self.screen.blit(self.about_background, (0, 0))
        text_surf, text_rect = self.font.render("PROGRAMMERS", TOMATO)
        self.screen.blit(text_surf, (240, 100))
        text_surf, text_rect = self.font.render("18127017 - Nguyen Hoang Nhan", TOMATO)
        self.screen.blit(text_surf, (150, 150))
        text_surf, text_rect = self.font.render("18127259 - Kieu Cong Hau", TOMATO)
        self.screen.blit(text_surf, (150, 200))
        text_surf, text_rect = self.font.render("18127267 - Tran Dinh Sang", TOMATO)
        self.screen.blit(text_surf, (150, 250))
        text_surf, text_rect = self.font.render("18127268 - Tran Thanh Tam", TOMATO)
        self.screen.blit(text_surf, (150, 300))


    def level_draw(self):
        self.level_background = self.home_background
        self.screen.fill(BLACK)
        self.screen.blit(self.level_background, (0, 0))


    def setting_draw(self):
        self.screen.fill(BLACK)


    def setting_event(self):
        if self.current_map == 1:
            self.map_1 = pygame.transform.scale(self.map_1, (MAP_WIDTH, MAP_HEIGHT))
            self.screen.blit(self.map_1, (ROW_PADDING // 2, 0))
        elif self.current_map == 2:
            self.map_2 = pygame.transform.scale(self.map_2, (MAP_WIDTH, MAP_HEIGHT))
            self.screen.blit(self.map_2, (ROW_PADDING // 2, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 255 <= self.mouse[0] <= 355 and 620 <= self.mouse[1] <= 670:
                    self.state = STATE_HOME
                elif 360 <= self.mouse[0] <= 403.3 and 620 <= self.mouse[1] <= 670:
                    if self.current_map < 2:
                        self.current_map += 1
                elif 206.7 <= self.mouse[0] <= 250 and 620 <= self.mouse[1] <= 670:
                    if self.current_map > 1:
                        self.current_map -= 1

        self.mouse = pygame.mouse.get_pos()
        if 255 <= self.mouse[0] <= 355 and 620 <= self.mouse[1] <= 670:
            self.draw_button(self.screen, OK_POS, DARK_COLOR, RED, "OK")
        else:
            self.draw_button(self.screen, OK_POS, LIGHT_COLOR, BLACK, "OK")
        if 360 <= self.mouse[0] <= 403.3 and 620 <= self.mouse[1] <= 670:
            self.draw_triangle_button(self.screen, TRIANGLE_1_POS, DARK_COLOR)
        else:
            self.draw_triangle_button(self.screen, TRIANGLE_1_POS, LIGHT_COLOR)
        if 206.7 <= self.mouse[0] <= 250 and 620 <= self.mouse[1] <= 670:
            self.draw_triangle_button(self.screen, TRIANGLE_2_POS, DARK_COLOR)
        else:
            self.draw_triangle_button(self.screen, TRIANGLE_2_POS, LIGHT_COLOR)
        pygame.display.update()


    def play_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
        pygame.display.update()


    def about_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 400 <= self.mouse[0] <= 600 and 560 <= self.mouse[1] <= 610:
                    self.state = STATE_HOME

        self.mouse = pygame.mouse.get_pos()
        if 400 <= self.mouse[0] <= 600 and 560 <= self.mouse[1] <= 610:
            self.draw_button(self.screen, BACK_POS, DARK_COLOR, RED, "Back")
        else:
            self.draw_button(self.screen, BACK_POS, LIGHT_COLOR, BLACK, "Back")
        pygame.display.update()


    def level_event(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 150 <= self.mouse[0] <= 450 and 320 <= self.mouse[1] <= 395:
                    self.state = STATE_PLAYING
                    self.difficult = 1
                elif 150 <= self.mouse[0] <= 450 and 400 <= self.mouse[1] <= 450:
                    self.state = STATE_PLAYING
                    self.difficult = 2
                elif 150 <= self.mouse[0] <= 450 and 480 <= self.mouse[1] <= 530:
                    self.state = STATE_PLAYING
                    self.difficult = 3
                elif 150 <= self.mouse[0] <= 450 and 560 <= self.mouse[1] <= 610:
                    self.state = STATE_PLAYING
                    self.difficult = 4
                elif 150 <= self.mouse[0] <= 450 and 600 <= self.mouse[1] <= 900:
                    self.state = STATE_HOME
            elif event.type == pygame.QUIT:
                self.is_running = False

        self.mouse = pygame.mouse.get_pos()
        if 150 <= self.mouse[0] <= 450 and 320 <= self.mouse[1] <= 375:
            self.draw_button(self.screen, LEVEL_1_POS, DARK_COLOR, RED, "Level 1")
        else:
            self.draw_button(self.screen, LEVEL_1_POS, LIGHT_COLOR, BLACK, "Level 1")
        if 150 <= self.mouse[0] <= 450 and 400 <= self.mouse[1] <= 450:
            self.draw_button(self.screen, LEVEL_2_POS, DARK_COLOR, RED, "Level 2")
        else:
            self.draw_button(self.screen, LEVEL_2_POS, LIGHT_COLOR, BLACK, "Level 2")
        if 150 <= self.mouse[0] <= 450 and 480 <= self.mouse[1] <= 530:
            self.draw_button(self.screen, LEVEL_3_POS, DARK_COLOR, RED, "Level 3")
        else:
            self.draw_button(self.screen, LEVEL_3_POS, LIGHT_COLOR, BLACK, "Level 3")
        if 150 <= self.mouse[0] <= 450 and 560 <= self.mouse[1] <= 610:
            self.draw_button(self.screen, LEVEL_4_POS, DARK_COLOR, RED, "Level 4")
        else:
            self.draw_button(self.screen, LEVEL_4_POS, LIGHT_COLOR, BLACK, "Level 4")
        if 150 <= self.mouse[0] <= 450 and 600 <= self.mouse[1] <= 900:
            self.draw_button(self.screen, BACK_LEVEL_POS, DARK_COLOR, RED, "Back")
        else:
            self.draw_button(self.screen, BACK_LEVEL_POS, LIGHT_COLOR, BLACK, "Back")
        pygame.display.update()


    def init_event(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 150 <= self.mouse[0] <= 450 and 320 <= self.mouse[1] <= 395:
                    self.state = STATE_LEVEL
                elif 150 <= self.mouse[0] <= 450 and 400 <= self.mouse[1] <= 450:
                    self.state = STATE_SETTING
                elif 150 <= self.mouse[0] <= 450 and 480 <= self.mouse[1] <= 530:
                    self.state = STATE_ABOUT
                elif 150 <= self.mouse[0] <= 450 and 560 <= self.mouse[1] <= 610:
                    self.is_running = False
            elif event.type == pygame.QUIT:
                self.is_running = False

        self.mouse = pygame.mouse.get_pos()
        if 150 <= self.mouse[0] <= 450 and 320 <= self.mouse[1] <= 375:
            self.draw_button(self.screen, START_POS, DARK_COLOR, RED, "Start")
        else:
            self.draw_button(self.screen, START_POS, LIGHT_COLOR, BLACK, "Start")
        if 150 <= self.mouse[0] <= 450 and 400 <= self.mouse[1] <= 450:
            self.draw_button(self.screen, SETTING_POS, DARK_COLOR, RED, "Setting")
        else:
            self.draw_button(self.screen, SETTING_POS, LIGHT_COLOR, BLACK, "Setting")
        if 150 <= self.mouse[0] <= 450 and 480 <= self.mouse[1] <= 530:
            self.draw_button(self.screen, ABOUT_POS, DARK_COLOR, RED, "About")
        else:
            self.draw_button(self.screen, ABOUT_POS, LIGHT_COLOR, BLACK, "About")
        if 150 <= self.mouse[0] <= 450 and 560 <= self.mouse[1] <= 610:
            self.draw_button(self.screen, EXIT_POS, DARK_COLOR, RED, "Exit")
        else:
            self.draw_button(self.screen, EXIT_POS, LIGHT_COLOR, BLACK, "Exit")
        pygame.display.update()


    def run(self):
        while self.is_running:
            if self.state == STATE_HOME:
                self.home_draw()
                self.init_event()
            elif self.state == STATE_PLAYING:
                self.play_draw()
                self.launch_pacman_game()
                self.play_event()
            elif self.state == STATE_ABOUT:
                self.about_draw()
                self.about_event()
            elif self.state == STATE_LEVEL:
                self.level_draw()
                self.level_event()
            elif self.state == STATE_SETTING:
                self.setting_draw()
                self.setting_event()
            else:
                self.is_running = False

        self.clock.tick(60)
        pygame.quit()
        sys.exit()
