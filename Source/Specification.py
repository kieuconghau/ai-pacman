# This is the file to declare the setting variables.
import pygame

# Window
APP_WIDTH, APP_HEIGHT = 610, 680
APP_CAPTION = r"Pacman"


# Map
MAP_IMG = [r"../Assets/map_0.png",
           r"../Assets/map_1.png"]
MAP_INPUT_TXT = [r"../Assets/map_0.txt",
                 r"../Assets/map_1.txt"]
MAP_NUM = len(MAP_IMG)


# Backgroud
HOME_BACKGROUND = r"../Assets/home_bg.png"
ABOUT_BACKGROUND = r"../Assets/about_bg.png"


# Screen state
STATE_HOME = "home"
STATE_PLAYING = "playing"
STATE_ABOUT = "about"
STATE_LEVEL = "level"
STATE_SETTING = "setting"


# Home screen
HOME_BG_WIDTH, HOME_BG_HEIGHT = APP_WIDTH, APP_HEIGHT - 410
START_POS = pygame.Rect(150, 325, 300, 50)
SETTING_POS = pygame.Rect(150, 405, 300, 50)
ABOUT_POS = pygame.Rect(150, 485, 300, 50)
EXIT_POS = pygame.Rect(150, 565, 300, 50)


# Level screen
LEVEL_1_POS = pygame.Rect(150, 320, 300, 50)
LEVEL_2_POS = pygame.Rect(150, 390, 300, 50)
LEVEL_3_POS = pygame.Rect(150, 460, 300, 50)
LEVEL_4_POS = pygame.Rect(150, 530, 300, 50)
BACK_LEVEL_POS = pygame.Rect(150, 600, 300, 50)


# About screen
BACK_POS = pygame.Rect(225, 530, 150, 50)


# Setting screen
OK_POS = pygame.Rect(255, 620, 100, 50)
TRIANGLE_1_POS = [[360, 620], [360, 670], [403.3, 645]]
TRIANGLE_2_POS = [[250, 620], [250, 670], [206.7, 645]]


# Play screen
ROW_PADDING, COL_PADDING = 50, 60
MAP_WIDTH, MAP_HEIGHT = APP_WIDTH - ROW_PADDING, APP_HEIGHT - COL_PADDING
MAP_POS_X, MAP_POS_Y = ROW_PADDING // 2, COL_PADDING * 2 // 3
CELL_SIZE = 20
ROW, COL = MAP_WIDTH // CELL_SIZE, MAP_HEIGHT // CELL_SIZE
SCORE_POS = (30, 10)
SPEED = 500


# Score
SCORE_BONUS = 20
SCORE_PENALTY = -1


# Font
FONT = r"../Fonts/8514fix.fon"


# Color
BACKGROUND_COLOR = (65, 98, 132)
LIGHT_GREY = (170, 170, 170)
DARK_GREY = (75, 75, 75)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
TOMATO = (255, 99, 71)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
