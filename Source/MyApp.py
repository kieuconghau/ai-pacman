import sys
import pygame.freetype
import Pacman
import Food
import Monster
import Map
import GraphSearchAStar
from Specification import *


class MyApp:
    ################################################## CORE FUNCTIONS ##################################################
    def __init__(self):
        pygame.init()

        self.font = pygame.freetype.Font(FONT)
        self.screen = pygame.display.set_mode((APP_WIDTH, APP_HEIGHT))
        self.caption = pygame.display.set_caption(APP_CAPTION)

        self.current_map_index = 0
        self.current_level = 1
        self.score = 0

        self.map = pygame.image.load(MAP_IMG[self.current_map_index])
        self.map = pygame.transform.scale(self.map, (MAP_WIDTH, MAP_HEIGHT))
        self.home_background = pygame.image.load(HOME_BACKGROUND)
        self.home_background = pygame.transform.scale(self.home_background, (HOME_BG_WIDTH, HOME_BG_HEIGHT))
        self.about_background = pygame.image.load(ABOUT_BACKGROUND)
        self.about_background = pygame.transform.scale(self.about_background, (APP_WIDTH, APP_HEIGHT))
        self.level_background = self.home_background
        self.gameover_background = pygame.image.load(GAMEOVER_BACKGROUND)
        self.gameover_background = pygame.transform.scale(self.gameover_background, (GAMEOVER_BACKGROUND_WIDTH, GAMEOVER_BACKGROUND_HEIGHT))
        self.coin = pygame.image.load(COIN_IMAGE)
        self.coin = pygame.transform.scale(self.coin, (COIN_WIDTH, COIN_HEIGHT))
        self.victory_background = pygame.image.load(VICTORY_BACKGROUND)
        self.victory_background = pygame.transform.scale(self.victory_background, (VICTORY_WIDTH, VICTORY_HEIGHT))
        self.pacman1 = pygame.image.load(PACMAN1)
        self.pacman1 = pygame.transform.scale(self.pacman1, (PACMAN_WIDTH, PACMAN_HEIGHT))
        self.pacman2 = pygame.image.load(PACMAN2)
        self.pacman2 = pygame.transform.scale(self.pacman2, (PACMAN_WIDTH, PACMAN_HEIGHT))
        self.pacman3 = pygame.image.load(PACMAN3)
        self.pacman3 = pygame.transform.scale(self.pacman3, (PACMAN_WIDTH, PACMAN_HEIGHT))
        self.pacman4 = pygame.image.load(PACMAN4)
        self.pacman4 = pygame.transform.scale(self.pacman4, (PACMAN_WIDTH, PACMAN_HEIGHT))
        self.pacman5 = pygame.image.load(PACMAN5)
        self.pacman5 = pygame.transform.scale(self.pacman5, (PACMAN_WIDTH, PACMAN_HEIGHT))

        self.state = STATE_HOME
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.mouse = None


    def launch_pacman_game(self):
        """
        Launch the Pacman game with the corresponding level and map.
        """
        pygame.display.update()
        self.score = 0
        self.draw_score()

        if self.current_level == 1:
            self.level_1()
        elif self.current_level == 2:
            self.level_2()
        elif self.current_level == 3:
            self.level_3()
        elif self.current_level == 4:
            self.level_4()


    def level_1(self):
        """
        Level 1: Pac-man know the food’s position in map and monsters do not appear in map.
        There is only one food in the map.
        """
        graph_map, pacman_pos, food_pos = Map.read_map_level_1(MAP_INPUT_TXT[self.current_level - 1][self.current_map_index])
        path = GraphSearchAStar.search(graph_map, pacman_pos, food_pos)

        pacman = Pacman.Pacman(self, pacman_pos)
        pacman.appear()

        food = Food.Food(self, food_pos)
        food.appear()

        self.ready()

        if path is not None:
            goal = path[-1]
            path = path[1:-1]

            for cell in path:
                pacman.move(cell)
                self.score += SCORE_PENALTY
                self.draw_score()
                pygame.time.delay(SPEED)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.is_running = False

            pacman.move(goal)
            self.score += SCORE_PENALTY + SCORE_BONUS
            self.draw_score()
            self.state = STATE_VICTORY
        else:
            self.state = STATE_GAMEOVER

        pygame.time.delay(1000)


    def level_2(self):
        """
        Level 2: monsters stand in the place ever (never move around).
        If Pac-man pass through the monster or vice versa, game is over.
        There is still one food in the map and Pac-man know its position.
        """
        graph_map, pacman_pos, food_pos, monster_pos_list =\
            Map.read_map_level_2(MAP_INPUT_TXT[self.current_level - 1][self.current_map_index], monster_as_wall=True)

        path = GraphSearchAStar.search(graph_map, pacman_pos, food_pos)

        pacman = Pacman.Pacman(self, pacman_pos)
        pacman.appear()

        food = Food.Food(self, food_pos)
        food.appear()

        monster_list = [Monster.Monster(self, monster_pos) for monster_pos in monster_pos_list]
        for monster in monster_list:
            monster.appear()

        if path is None:
            graph_map, pacman_pos, food_pos, monster_pos_list = \
                Map.read_map_level_2(MAP_INPUT_TXT[self.current_level - 1][self.current_map_index],
                                     monster_as_wall=False)

            path = GraphSearchAStar.search(graph_map, pacman_pos, food_pos)

            if path is not None:
                self.ready()

                path = path[1:]

                for cell in path:
                    pacman.move(cell)
                    self.score += SCORE_PENALTY
                    self.draw_score()

                    if cell in monster_pos_list:
                        break

                    pygame.time.delay(SPEED)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.is_running = False

            self.state = STATE_GAMEOVER
        else:
            self.ready()

            goal = path[-1]
            path = path[1:-1]

            for cell in path:
                pacman.move(cell)
                self.score += SCORE_PENALTY
                self.draw_score()
                pygame.time.delay(SPEED)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.is_running = False

            pacman.move(goal)
            self.score += SCORE_PENALTY + SCORE_BONUS
            self.draw_score()
            self.state = STATE_VICTORY

        pygame.time.delay(1000)


    def level_3(self):
        """
        Level 3: Pac-man cannot see the foods if they are outside Pacman’s nearest threestep.
        It means that Pac-man just only scan all the adjacent him (8 tiles x 3).
        There are many foods in the map.
        Monsters just move one step in any valid direction (if any) around the initial location at the start of the game.
        Each step Pacman go, each step Monsters move.
        """
        pygame.time.delay(1000)
        self.state = STATE_GAMEOVER

    def level_4(self):
        """
        Level 4 (difficult): map is opened.
        Monsters will seek and kill Pac-man.
        Pac-man want to get food as much as possible.
        Pacman will die if at least one monster passes him.
        It is ok for monsters go through each other.
        Each step Pacman go, each step Monsters move.
        The food is so many.
        """
        pygame.time.delay(1000)
        self.state = STATE_GAMEOVER


    def run(self):
        """
        Run this program.
        """
        while self.is_running:
            if self.state == STATE_HOME:
                self.home_draw()
                self.home_event()
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
            elif self.state == STATE_GAMEOVER:
                self.gameover_draw1()
                self.gameover_draw2()
                self.gameover_event()
            elif self.state == STATE_VICTORY:
                self.victory_draw1()
                self.victory_draw2()
                self.victory_draw3()
                self.victory_draw4()
                self.victory_draw5()
            else:
                self.is_running = False

        self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
    ####################################################################################################################


    def ready(self):
        """
        Ready effect (3, 2, 1, GO).
        """
        text_list = ['3', '2', '1', 'GO']
        for text in text_list:
            text_surf, text_rect = self.font.render(text, WHITE)

            text_pos = (READY_POS[0] - len(text)*5, READY_POS[1])
            text_rect[0] = text_pos[0]
            text_rect[1] = text_pos[1]

            self.screen.blit(text_surf, text_pos)
            pygame.display.update(text_rect)

            pygame.time.delay(1000)
            pygame.display.update(pygame.draw.rect(self.screen, BLACK, text_rect))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False


    def victory_draw1(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.victory_background, (50, 0))
        self.screen.blit(self.pacman1, (50, 350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 255 <= self.mouse[0] <= 355 and 620 <= self.mouse[1] <= 670:
                    self.state = STATE_HOME
        self.mouse = pygame.mouse.get_pos()
        if 255 <= self.mouse[0] <= 355 and 620 <= self.mouse[1] <= 670:
            self.draw_button(self.screen, OK_POS, DARK_GREY, RED, "OK")
        else:
            self.draw_button(self.screen, OK_POS, LIGHT_GREY, BLACK, "OK")
        pygame.time.delay(100)
        pygame.display.update()


    def victory_draw2(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.victory_background, (50, 0))
        self.screen.blit(self.pacman2, (125, 350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 255 <= self.mouse[0] <= 355 and 620 <= self.mouse[1] <= 670:
                    self.state = STATE_HOME
        self.mouse = pygame.mouse.get_pos()
        if 255 <= self.mouse[0] <= 355 and 620 <= self.mouse[1] <= 670:
            self.draw_button(self.screen, OK_POS, DARK_GREY, RED, "OK")
        else:
            self.draw_button(self.screen, OK_POS, LIGHT_GREY, BLACK, "OK")
        pygame.time.delay(100)
        pygame.display.update()


    def victory_draw3(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.pacman3, (200, 350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 255 <= self.mouse[0] <= 355 and 620 <= self.mouse[1] <= 670:
                    self.state = STATE_HOME
        self.mouse = pygame.mouse.get_pos()
        if 255 <= self.mouse[0] <= 355 and 620 <= self.mouse[1] <= 670:
            self.draw_button(self.screen, OK_POS, DARK_GREY, RED, "OK")
        else:
            self.draw_button(self.screen, OK_POS, LIGHT_GREY, BLACK, "OK")
        pygame.time.delay(100)
        pygame.display.update()


    def victory_draw4(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.victory_background, (50, 0))
        self.screen.blit(self.pacman4, (275, 350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 255 <= self.mouse[0] <= 355 and 620 <= self.mouse[1] <= 670:
                    self.state = STATE_HOME
        self.mouse = pygame.mouse.get_pos()
        if 255 <= self.mouse[0] <= 355 and 620 <= self.mouse[1] <= 670:
            self.draw_button(self.screen, OK_POS, DARK_GREY, RED, "OK")
        else:
            self.draw_button(self.screen, OK_POS, LIGHT_GREY, BLACK, "OK")
        pygame.time.delay(100)
        pygame.display.update()


    def victory_draw5(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.victory_background, (50, 0))
        self.screen.blit(self.pacman5, (350, 350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 255 <= self.mouse[0] <= 355 and 620 <= self.mouse[1] <= 670:
                    self.state = STATE_HOME
        self.mouse = pygame.mouse.get_pos()
        if 255 <= self.mouse[0] <= 355 and 620 <= self.mouse[1] <= 670:
            self.draw_button(self.screen, OK_POS, DARK_GREY, RED, "OK")
        else:
            self.draw_button(self.screen, OK_POS, LIGHT_GREY, BLACK, "OK")
        pygame.time.delay(100)
        pygame.display.update()


    def gameover_draw1(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.gameover_background, (0, 0))
        self.screen.blit(self.coin, COIN_POS)
        pygame.time.delay(350)
        pygame.display.update()


    def gameover_draw2(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.gameover_background, (0, 0))
        pygame.time.delay(350)

     
    def gameover_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 200 <= self.mouse[0] <= 400 and 430 <= self.mouse[1] <= 630:
                    self.state = STATE_HOME
        self.mouse = pygame.mouse.get_pos()

        pygame.display.update()


    def draw_score(self):
        """
        Display the current score.
        """
        text_surf, text_rect = self.font.render("SCORES: " + str(self.score), WHITE)

        text_rect[0] = SCORE_POS[0]
        text_rect[1] = SCORE_POS[1]

        pygame.draw.rect(self.screen, BLACK, text_rect)
        self.screen.blit(text_surf, SCORE_POS)
        pygame.display.update(text_rect)


    def draw_grids(self):
        """
        Draw the grid onto the map for better designing.
        """
        for x in range(int(MAP_WIDTH / CELL_SIZE) + 1):
            self.screen.blit(self.font.render(str(x % 10), WHITE)[0],
                             (x*CELL_SIZE + MAP_POS_X + CELL_SIZE//4, MAP_POS_Y - CELL_SIZE))

            pygame.draw.line(self.screen, (107, 107, 107),
                             (x*CELL_SIZE + MAP_POS_X, MAP_POS_Y),
                             (x * CELL_SIZE + MAP_POS_X, MAP_HEIGHT + MAP_POS_Y))

        for y in range(int(MAP_HEIGHT / CELL_SIZE) + 1):
            self.screen.blit(self.font.render(str(y % 10), WHITE)[0],
                             (MAP_POS_X - CELL_SIZE, y*CELL_SIZE + MAP_POS_Y))

            pygame.draw.line(self.screen, (107, 107, 107),
                             (MAP_POS_X, y*CELL_SIZE + MAP_POS_Y),
                             (MAP_WIDTH + MAP_POS_X, y * CELL_SIZE + MAP_POS_Y))


    def draw_button(self, surf, rect, button_color, text_color, text):
        pygame.draw.rect(surf, button_color, rect)
        text_surf, text_rect = self.font.render(text, text_color)
        text_rect.center = rect.center
        self.screen.blit(text_surf, text_rect)


    @staticmethod
    def draw_triangle_button(surf, rect, button_color):
        pygame.draw.polygon(surf, button_color, rect)


    def home_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.home_background, (0, 0))


    def play_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.map, (MAP_POS_X, MAP_POS_Y))


    def about_draw(self):
        self.screen.fill(BLACK)
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
        self.screen.fill(BLACK)
        self.screen.blit(self.level_background, (0, 0))


    def setting_draw(self):
        self.screen.fill(BLACK)


    def setting_event(self):
        self.map = pygame.transform.scale(self.map, (MAP_WIDTH, MAP_HEIGHT))
        self.screen.blit(self.map, (ROW_PADDING // 2, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 255 <= self.mouse[0] <= 355 and 620 <= self.mouse[1] <= 670:
                    self.state = STATE_HOME
                elif 360 <= self.mouse[0] <= 403.3 and 620 <= self.mouse[1] <= 670:
                    self.current_map_index += 1
                    self.current_map_index %= MAP_NUM
                elif 206.7 <= self.mouse[0] <= 250 and 620 <= self.mouse[1] <= 670:
                    self.current_map_index += MAP_NUM - 1
                    self.current_map_index %= MAP_NUM
                self.map = pygame.image.load(MAP_IMG[self.current_map_index])


        self.mouse = pygame.mouse.get_pos()
        if 255 <= self.mouse[0] <= 355 and 620 <= self.mouse[1] <= 670:
            self.draw_button(self.screen, OK_POS, DARK_GREY, RED, "OK")
        else:
            self.draw_button(self.screen, OK_POS, LIGHT_GREY, BLACK, "OK")
        if 360 <= self.mouse[0] <= 403.3 and 620 <= self.mouse[1] <= 670:
            self.draw_triangle_button(self.screen, TRIANGLE_1_POS, DARK_GREY)
        else:
            self.draw_triangle_button(self.screen, TRIANGLE_1_POS, LIGHT_GREY)
        if 206.7 <= self.mouse[0] <= 250 and 620 <= self.mouse[1] <= 670:
            self.draw_triangle_button(self.screen, TRIANGLE_2_POS, DARK_GREY)
        else:
            self.draw_triangle_button(self.screen, TRIANGLE_2_POS, LIGHT_GREY)
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
                if 225 <= self.mouse[0] <= 375 and 530 <= self.mouse[1] <= 580:
                    self.state = STATE_HOME

        self.mouse = pygame.mouse.get_pos()
        if 225 <= self.mouse[0] <= 375 and 530 <= self.mouse[1] <= 580:
            self.draw_button(self.screen, BACK_POS, DARK_GREY, RED, "Back")
        else:
            self.draw_button(self.screen, BACK_POS, LIGHT_GREY, BLACK, "Back")
        pygame.display.update()


    def level_event(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 150 <= self.mouse[0] <= 450 and 320 <= self.mouse[1] <= 370:
                    self.state = STATE_PLAYING
                    self.current_level = 1
                elif 150 <= self.mouse[0] <= 450 and 390 <= self.mouse[1] <= 440:
                    self.state = STATE_PLAYING
                    self.current_level = 2
                elif 150 <= self.mouse[0] <= 450 and 460 <= self.mouse[1] <= 510:
                    self.state = STATE_PLAYING
                    self.current_level = 3
                elif 150 <= self.mouse[0] <= 450 and 530 <= self.mouse[1] <= 580:
                    self.state = STATE_PLAYING
                    self.current_level = 4
                elif 150 <= self.mouse[0] <= 450 and 600 <= self.mouse[1] <= 650:
                    self.state = STATE_HOME
            elif event.type == pygame.QUIT:
                self.is_running = False

        self.mouse = pygame.mouse.get_pos()
        if 150 <= self.mouse[0] <= 450 and 320 <= self.mouse[1] <= 370:
            self.draw_button(self.screen, LEVEL_1_POS, DARK_GREY, RED, "Level 1")
        else:
            self.draw_button(self.screen, LEVEL_1_POS, LIGHT_GREY, BLACK, "Level 1")
        if 150 <= self.mouse[0] <= 450 and 390 <= self.mouse[1] <= 440:
            self.draw_button(self.screen, LEVEL_2_POS, DARK_GREY, RED, "Level 2")
        else:
            self.draw_button(self.screen, LEVEL_2_POS, LIGHT_GREY, BLACK, "Level 2")
        if 150 <= self.mouse[0] <= 450 and 460 <= self.mouse[1] <= 510:
            self.draw_button(self.screen, LEVEL_3_POS, DARK_GREY, RED, "Level 3")
        else:
            self.draw_button(self.screen, LEVEL_3_POS, LIGHT_GREY, BLACK, "Level 3")
        if 150 <= self.mouse[0] <= 450 and 530 <= self.mouse[1] <= 580:
            self.draw_button(self.screen, LEVEL_4_POS, DARK_GREY, RED, "Level 4")
        else:
            self.draw_button(self.screen, LEVEL_4_POS, LIGHT_GREY, BLACK, "Level 4")
        if 150 <= self.mouse[0] <= 450 and 600 <= self.mouse[1] <= 650:
            self.draw_button(self.screen, BACK_LEVEL_POS, DARK_GREY, RED, "Back")
        else:
            self.draw_button(self.screen, BACK_LEVEL_POS, LIGHT_GREY, BLACK, "Back")
        pygame.display.update()


    def home_event(self):
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
            self.draw_button(self.screen, START_POS, DARK_GREY, RED, "Start")
        else:
            self.draw_button(self.screen, START_POS, LIGHT_GREY, BLACK, "Start")
        if 150 <= self.mouse[0] <= 450 and 400 <= self.mouse[1] <= 450:
            self.draw_button(self.screen, SETTING_POS, DARK_GREY, RED, "Setting")
        else:
            self.draw_button(self.screen, SETTING_POS, LIGHT_GREY, BLACK, "Setting")
        if 150 <= self.mouse[0] <= 450 and 480 <= self.mouse[1] <= 530:
            self.draw_button(self.screen, ABOUT_POS, DARK_GREY, RED, "About")
        else:
            self.draw_button(self.screen, ABOUT_POS, LIGHT_GREY, BLACK, "About")
        if 150 <= self.mouse[0] <= 450 and 560 <= self.mouse[1] <= 610:
            self.draw_button(self.screen, EXIT_POS, DARK_GREY, RED, "Exit")
        else:
            self.draw_button(self.screen, EXIT_POS, LIGHT_GREY, BLACK, "Exit")
        pygame.display.update()
