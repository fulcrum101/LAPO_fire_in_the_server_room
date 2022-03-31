#import pygame
import codecs
import random
from collections import defaultdict
from menu import Menu
class Quizz(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.game = game
        self.points = {}
        self.questions = None
        self.read_points()
        self.state=0
        self.fail = False
        self.q = None
        self.correct_ans = None

    def read_points(self):
        '''
        Reads in all points questions and answers from .txt file.
        '''
        d = defaultdict(list)
        text = []
        with codecs.open("quizz_controlpoints.txt", encoding='utf-8') as f:
            for line in f:
                text.append(line.rstrip())
        index = None
        switch = True # True - reads question, false - answer
        for i, x in enumerate(text):
            if x[0] == '*':
                index = int(x[1:])
            elif switch:
                d[index].append((x, text[i+1].split(';')))
                switch = not switch
            else: # line is an answer
                switch = not switch

        self.questions = d

    def ControlPointQuizz(self, index:int):
        '''
        Displays question + answer.
        EXCLUDING CHARGE STATIONS.
        :param index: index of Control
        :return: None
        '''
        self.max_points = self.game.MAX_POINTS_Q
        self.start(index)

    def start(self, index:int):
        '''
        Main quizz loop.
        '''
        self.run_display = True
        if index not in self.questions:
            raise KeyError(
                'Index of checkpoint not found. Please check if the function was not used for charging station.')
        if len(self.questions[index])!=1:
            self.q = random.choice(self.questions[index])
        else:
            self.q = self.questions[index][0]
        self.correct_ans = self.q[1][0]
        random.shuffle(self.q[1])  # shuffles the answers
        for x in self.q[1]:
            x.replace(' ', '')
        if len(self.q[1]) != 3:
            raise ValueError('Answers of question are not completed. Please check if source file is allright.')
        while self.run_display:
            self.game.check_events()
            if self.fail:
                self.fail = False
                self.max_points = max(0, self.max_points - 50)
                self.start(index)

            self.game.display.fill(self.game.BLACK)
            self.game.draw_text(self.q[0], 25, self.mid_w, 200)
            self.game.draw_text(self.q[1][0], 25, self.mid_w, self.mid_h - 35)
            self.game.draw_text(self.q[1][1], 25, self.mid_w, self.mid_h)
            self.game.draw_text(self.q[1][2], 25, self.mid_w, self.mid_h + 35)
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
            if self.q[1][self.state]==self.correct_ans:
                print(f'Pareizi! + {self.max_points} punkti.')
                self.run_display = False

            else:
                print(f'Nav areizi! Pameģeniet vēlreiz.')
                print(f'Tagad Jūs maksimāli varat iegūt {self.max_points} punktus.')
                self.fail = True

