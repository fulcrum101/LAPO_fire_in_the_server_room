#import pygame
import codecs
import random
from collections import defaultdict
from menu import Menu

class ChargeQuizz(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.game = game
        self.state=0
        self.fail = False
        self.a, self.b = None, None
        self.cost = 750
        self.answers = None

    def StationQuizz(self):
        '''
        Displays question + answer.
        EXCLUDING CHARGE STATIONS.
        :param index: index of Control
        :return: None
        '''
        self.start()

    def start(self):
        '''
        Main quizz loop.
        '''
        self.a, self.b = random.randint(1, 10), random.randint(1, 10)
        self.answers=[str(self.a*self.b)]
        self.answers.append(str(random.randint(1, 10)*random.randint(1, 10)))
        self.answers.append(str(random.randint(1, 10) * random.randint(1, 10)))
        random.shuffle(self.answers)
        while self.run_display:
            self.game.check_events()
            if self.fail:
                self.fail = False
                self.cost = min(self.game.POINTS, self.cost + 50)
                print(f'Tagad pilna uzladēšanas cena ir {self.cost} punkti.')
                self.start()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text(f'Cik būs {self.a} x {self.b}?', 25, self.mid_w, 200)
            self.game.draw_text(self.answers[0], 25, self.mid_w, self.mid_h - 35)
            self.game.draw_text(self.answers[1], 25, self.mid_w, self.mid_h)
            self.game.draw_text(self.answers[2], 25, self.mid_w, self.mid_h + 35)
            self.check_input()
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        """
        Listens for the keyboard event (keys pressed) and moves cursor (*) accordingly.
        """
        match self.state:
            case 0:
                self.cursor_rect.midtop = (450, self.mid_h - 35)
            case 1:
                self.cursor_rect.midtop = (450, self.mid_h)
            case 2:
                self.cursor_rect.midtop = (450, self.mid_h + 35)

    def check_input(self):
        self.move_cursor()
        #print(self.state)
        if self.game.DOWN_KEY:
            if self.state == 2:
                self.state = 0
            else:
                self.state+=1
        elif self.game.UP_KEY:
            if self.state == 0:
                self.state = 2
            else:
                self.state+=1
        elif self.game.START_KEY:
            if self.answers[self.state]==str(self.a*self.b):
                print(f'Pareizi! Auto pilnīgi uzladēts par {self.cost} punktiem.')
                self.game.POINTS-=self.cost
                self.game.CHARGE_LEVEL=100
                print(f'Tagad Jums ir {self.game.POINTS} punkti.')
                self.run_display = False
            else:
                print(f'Nav pareizi! Pameģeniet vēlreiz.')
                self.fail = True