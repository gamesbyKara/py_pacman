import pygame, sys
from settings import *


pygame.init()
vec = pygame.math.Vector2


class App:
  def __init__(self):
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    self.clock = pygame.time.Clock()
    self.running = True
    self.state = 'start'

  def run(self):
    while self.running:
      if self.state == 'start':
        self.start_events()
        self.start_update()
        self.start_draw()
      elif self.state == 'playing':
        self.playing_events()
        self.playing_update()
        self.playing_draw()
      else:
        self.running = False
      self.clock.tick(FPS)
    pygame.quit()
    sys.exit()

#@======================================HELPER FUNCTIONS==========================================

  def draw_text(self, words, screen, pos, size, color, font_name, centered = False):
    font = pygame.font.SysFont(font_name, size)
    text = font.render(words, False, color)
    text_size = text.get_size()
    if centered:
      pos[0] = pos[0]-text_size[0]//2
      pos[1] = pos[1]-text_size[1]//2
    screen.blit(text, pos)


#@========================================START FUNCTIONS=========================================
  def start_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
      if event.type == pygame.KEYDOWN and event.key ==pygame.K_SPACE:
        self.state = 'playing'

  def start_update(self):
    pass

  def start_draw(self):
    self.screen.fill(BLACK)
    self.draw_text('HIGH SCORE', self.screen, [5, 2], START_TEXT_SIZE, (255,255,255), START_FONT)
    self.draw_text('PAC-MAN', self.screen, [WIDTH//2, HEIGHT//2 - 150], TITLE_TEXT_SIZE, (255,255,0), START_FONT,centered=True)
    self.draw_text('PUSH SPACE TO START', self.screen, [WIDTH//2, HEIGHT//2], START_TEXT_SIZE, (252, 141, 104), START_FONT, centered=True)
    self.draw_text('1 PLAYER GAME', self.screen, [WIDTH//2, HEIGHT//2+75], START_TEXT_SIZE, (0,255,255), START_FONT, centered=True)
    self.draw_text('© Games By Kara', self.screen, [WIDTH//2, HEIGHT//2+250], START_TEXT_SIZE, (216,191,216), START_FONT, centered=True)
    pygame.display.update()


#@=====================================PLAYING FUNCTIONS=========================================

  def playing_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False

  def playing_update(self):
    pass

  def playing_draw(self):
    self.screen.fill(RED)
    pygame.display.update()