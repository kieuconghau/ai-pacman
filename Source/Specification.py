# This is the file to declare the setting variables.
import pygame

# Window
APP_WIDTH, APP_HEIGHT = 610, 680
APP_CAPTION = r"Pacman"
FPS = 60


# Map
MAP_IMG = [r"../Assets/map_1.png",
           r"../Assets/map_2.png"]
MAP_INPUT_TXT = [[r"../Assets/level_1/map_1.txt", r"../Assets/level_1/map_2.txt"],
                 [r"../Assets/level_2/map_1.txt", r"../Assets/level_2/map_2.txt"],
                 [r"../Assets/level_3/map_1.txt", r"../Assets/level_3/map_2.txt"],
                 [r"../Assets/level_4/map_1.txt", r"../Assets/level_4/map_2.txt"]]
MAP_NUM = len(MAP_IMG)


# Background
HOME_BACKGROUND = r"../Assets/home_bg.png"
ABOUT_BACKGROUND = r"../Assets/about_bg.png"
GAMEOVER_BACKGROUND = r"../Assets/gameover_bg.png"
VICTORY_BACKGROUND = r"../Assets/victory.jpg"

# Image
COIN_IMAGE = r"../Assets/coin.jpg"
# Screen state
STATE_HOME = "home"
STATE_PLAYING = "playing"
STATE_ABOUT = "about"
STATE_LEVEL = "level"
STATE_SETTING = "setting"
STATE_GAMEOVER = "gameover"
STATE_VICTORY = 'victory'


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
SCORE_POS = (30, 10)
READY_POS = (APP_WIDTH // 2, 10)

CELL_SIZE = 20
ROW, COL = MAP_WIDTH // CELL_SIZE, MAP_HEIGHT // CELL_SIZE

SPEED = 100


# Gameover screen
COIN_POS = (200, 430)
COIN_WIDTH, COIN_HEIGHT = (200, 200)
GAMEOVER_BACKGROUND_WIDTH, GAMEOVER_BACKGROUND_HEIGHT = HOME_BG_WIDTH, HOME_BG_HEIGHT + 300

# Victory screen
PACMAN1 = r"../Assets/pacman1.png"
PACMAN2 = r"../Assets/pacman2.png"
PACMAN3 = r"../Assets/pacman3.png"
PACMAN4 = r"../Assets/pacman4.png"
PACMAN5 = r"../Assets/pacman5.png"
VICTORY_WIDTH, VICTORY_HEIGHT = (500, 400)
PACMAN_WIDTH, PACMAN_HEIGHT = (500, 280)

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
