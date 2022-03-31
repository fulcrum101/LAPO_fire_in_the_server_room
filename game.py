import pygame
from menu import MainMenu, OptionsMenu, CreditsMenu, CarMenu
from map import Map
from car_game import CarGame
from pygame import mixer
import sys, time
from connect_to_leaderboard import upload_result
import codecs
from quizz import Quizz
from quizz_chargingstation import ChargeQuizz
class Game:
    def __init__(self):
        """
        Initialize Game object.
        Main object for the game.
        """
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.LEFT_KEY, self.RIGHT_KEY = False, False
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
        mixer.init()
        mixer.music.load("audio/tunetank.com_5524_summer-chill_by_cloudsystem.mp3")
        self.SOUND_VOLUME = 10
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.car_menu = CarMenu(self)
        self.curr_menu = self.main_menu #current menu
        self.quizz = Quizz(self)
        self.charge_quizz = ChargeQuizz(self)
        self.map_running = False
        self.car = None
        self.map = Map(self)
        self.car_game = CarGame(self)
        self.POINTS = 500
        self.CHARGE_LEVEL = 100 #charge percent
        mixer.music.set_volume(self.SOUND_VOLUME)
        mixer.music.play(-1)
        self.start_time = None
        self.end_time=None
        self.NAME=None
        self.MAX_POINTS_Q = 250 # Max points given for one question
        
        self.activePointI =-1
        self.activeRaceDone = 0
        self.activeQuizzDone = 0
        #note: lai tiktu pie ID self.map.ids[self.activePointI] 


    def game_loop(self):
        """
        Main game loop.
        """
        self.start_time = time.time()
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = True

            self.end_time = time.time()
            self.display.fill(self.BLACK)
            self.draw_text('Thanks for playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0, 0))
            pygame.display.update() # flush
            self.reset_keys()
            pygame.display.quit()
            pygame.quit()
            print(f"Jūsu punktu skaits: {self.POINTS}.")
            print(f"Jūsu laiks: {self.end_time-self.start_time}.")
            self.NAME = input("Kāds ir Jūsu vārds? - ")
            upload_result(self.NAME, self.POINTS, self.end_time-self.start_time)
            sys.exit()



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
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_n:
                    self.print_noteikumi()

    def reset_keys(self):
        """
        Resets pressed keys.
        """
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.LEFT_KEY, self.RIGHT_KEY = False, False

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

    def print_noteikumi(self):
        text=""
        with codecs.open("noteikumi.txt", encoding='utf-8') as f:
            for line in f:
                text+=line
        print(text)




