import pygame
import random
from time import time

class CarGame():
    def __init__(self, game):
        self.movement_done = 0
        self.game = game
        self.running = True
        self.crash = False
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.x_pos = [285, 395, 505, 615]
        self.car_x = self.x_pos[-1]
        self.car_y = self.mid_h*2 - 350
        self.enemy_cars = [pygame.transform.scale(i, (100, 200)) for i in self.game.car_menu.cars]
        self.enemy_car_speed = 20
        self.enemy_car_img = self.enemy_cars[0]
        self.enemy_car_startx = self.x_pos[0]
        self.enemy_car_starty = -100
        self.bgImg = pygame.image.load("images/race_game/race.png")



    def get_new_enemy_car(self):
        self.enemy_car_img = random.choice(self.enemy_cars)
        self.enemy_car_startx = random.choice(self.x_pos)

    def run_car(self, distance):
        starttime=time()
        while self.game.CHARGE_LEVEL != 0 and distance>(time()-starttime)/10:
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.bgImg, (0, 0))
            self.game.draw_text(f'Charge level: {self.game.CHARGE_LEVEL}%', 20, 100, 45)
            self.game.draw_text(f'Distance: {round(time()-starttime)/10}/{distance}', 20, 900, 45)
            self.game.display.blit(self.game.car, (self.car_x, self.car_y))
            self.game.check_events()
            self.check_input()

            self.run_enemy_car(self.enemy_car_startx, self.enemy_car_starty)
            self.enemy_car_starty += self.enemy_car_speed

            if self.enemy_car_starty > self.game.DISPLAY_H:
                self.enemy_car_starty = -200
                self.get_new_enemy_car()

            self.movement_done += 1

            car_rect = self.game.car.get_rect(topleft=(self.car_x, self.car_y))
            enemy_rect = self.enemy_car_img.get_rect(topleft=(self.enemy_car_startx, self.enemy_car_starty))
            if car_rect.colliderect(enemy_rect):

                self.game.CHARGE_LEVEL = int(self.game.CHARGE_LEVEL)-20
                if self.car_x == self.x_pos[0]:
                    self.car_x = self.x_pos[1]
                elif self.car_x == self.x_pos[-1]:
                    self.car_x = self.x_pos[-2]
                else:
                    self.car_x = self.x_pos[self.x_pos.index(self.car_x)+random.choice([-1,1])] #sets car_x to nearest other line
            if self.car_x < 275:
                self.game.CHARGE_LEVEL = int(self.game.CHARGE_LEVEL)-20
                self.car_x = 285
            elif self.car_x > 625:
                self.game.CHARGE_LEVEL = int(self.game.CHARGE_LEVEL)-20
                self.car_x = 615

            self.blit_screen()
        self.game.activeRaceDone = 1
        self.game.map.display_map()
        self.game.curr_menu = self.game.main_menu

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()  # flush
        self.game.reset_keys()

    def check_input(self):
        """
        Listens for keyboard events and changes car x position.
        """
        if self.game.BACK_KEY:
            self.running = False
            self.game.curr_menu = self.game.main_menu
        if self.game.RIGHT_KEY:
            self.car_x += 110
        elif self.game.LEFT_KEY:
            self.car_x -= 110

    def run_enemy_car(self, thingx, thingy):
        self.game.display.blit(self.enemy_car_img, (thingx, thingy))


