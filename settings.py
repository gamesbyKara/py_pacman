from pygame.math import Vector2 as vec

WIDTH, HEIGHT = 560, 620
FPS = 60
TOP_BOTTOM_BUFFER = 50
MAZE_WIDTH,MAZE_HEIGHT = WIDTH-TOP_BOTTOM_BUFFER, HEIGHT-TOP_BOTTOM_BUFFER

#color setting
BLACK = (0, 0, 0)
GREY = (77,77,77)
WHITE = (255,255,255)
YELLOW = (255,255,0)

CLYDE = (252, 141, 104)
INKY = (0,255,255)
BLINKY = (255,0,0)
PINKY = (216,191,216)

#font settings
TITLE_TEXT_SIZE = 30
START_TEXT_SIZE = 16
START_FONT = "Orbitron"


#player settings
PLAYER_START_POS = vec(14,23)

#enemy settings