# This is the file to declare the setting variables.
import pygame

# Window
MAP_WIDTH, MAP_HEIGHT = 560, 620
ROW_PADDING, COL_PADDING = 50, 60
MAP_POS_X, MAP_POS_Y = ROW_PADDING // 2, COL_PADDING // 3 * 2
APP_WIDTH, APP_HEIGHT = MAP_WIDTH + ROW_PADDING, MAP_HEIGHT + COL_PADDING
HOME_BG_WIDTH, HOME_BG_HEIGHT = APP_WIDTH, APP_HEIGHT - 410
APP_CAPTION = r"Pacman"

# Image
HOME_BACKGROUND = r"../Assets/home_bg.png"
ABOUT_BACKGROUND = r"../Assets/about_bg.png"
MAP_1 = r"../Assets/map_1.png"
MAP_2 = r"../Assets/map_2.png"

# Font
INIT_FONT = r"../Fonts/8514fix.fon"

# Color
BACKGROUND_COLOR = (65, 98, 132)
LIGHT_COLOR = (170, 170, 170)
DARK_COLOR = (75, 75, 75)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
TOMATO = (255, 99, 71)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Position
START_POS = pygame.Rect(150, 325, 300, 50)
SETTING_POS = pygame.Rect(150, 405, 300, 50)
ABOUT_POS = pygame.Rect(150, 485, 300, 50)
EXIT_POS = pygame.Rect(150, 565, 300, 50)

LEVEL_1_POS = pygame.Rect(150, 320, 300, 50)
LEVEL_2_POS = pygame.Rect(150, 390, 300, 50)
LEVEL_3_POS = pygame.Rect(150, 460, 300, 50)
LEVEL_4_POS = pygame.Rect(150, 530, 300, 50)

BACK_LEVEL_POS = pygame.Rect(150, 600, 300, 50)

BACK_POS = pygame.Rect(400, 560, 150, 50)

OK_POS = pygame.Rect(255, 620, 100, 50)
TRIANGLE_1_POS = [[360, 620], [360, 670], [403.3, 645]]
TRIANGLE_2_POS = [[250, 620], [250, 670], [206.7, 645]]

# Level
CURRENT_LEVEL = 1

# Screen state
STATE_HOME = "home"
STATE_PLAYING = "playing"
STATE_ABOUT = "about"
STATE_LEVEL = "level"
STATE_SETTING = "setting"
