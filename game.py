import pygame
from menu import MainMenu, OptionsMenu, CreditsMenu
from map import Map

class Game():
    def __init__(self):
        """
        Initialize Game object.
        Main object for the game.
        """
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1000, 1000
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H)) #create canvas
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        icon = pygame.image.load('images/icon.jpg')
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Tūrisma rallijs Liepāja 2022')
        self.font_name = 'consolas'
        self.BLACK, self.WHITE  = (0, 0, 0),(255, 255, 255)
        self.RED, self.GREEN, self.BLUE = (255,0,0), (0,255,0), (0,0,255)
        self.SKYBLUE, self.MAGENTA, self.YELLOW = (0,255, 255), (255, 0, 255), (255, 255, 0)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu #current menu
        self.map_running = False

    def game_loop(self):
        """
        Main game loop.
        """
        self.map = Map(self)
        self.map_running = True
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
                self.notplaying = True
            if self.map_running:
                self.map.run_map()
            self.reset_keys()
        while self.notplaying:
            self.check_events()
            if self.START_KEY:
                self.notplaying = False
                self.running = False
            self.display.fill(self.BLACK)
            self.draw_text('Thanks for playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0, 0))
            pygame.display.update() # flush
            self.reset_keys()

    def check_events(self):
        """
        Listens for keyboard events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        """
        Resets pressed keys.
        """
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        """
        Writes text to the screen.
        :param text: (str) Text needed to be written.
        :param size: (int) Text size.
        :param x: (int) X coordinate of where text will be written.
        :param y: (int) Y coordinate of where text will be written.
        """
        font = pygame.font.SysFont(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)




