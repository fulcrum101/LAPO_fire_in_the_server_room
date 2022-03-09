import pygame

class Menu():
    def __init__(self, game):
        """
        Initializes Menu object.
        
        :param game: (Game [game.py]) Main Game object.
        """
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2 ,  self.game.DISPLAY_H/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 45, 45) # x, y, width, height
        self.offset = -100

    def draw_cursor(self):
        """
        Draws cursor (* symbol).
        """
        self.game.draw_text('*', 45, self.cursor_rect.x - 20, self.cursor_rect.y)

    def blit_screen(self):
        """
        Resets screen + keys.
        """
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()  # flush
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        """
        Initialize MainMenu object.
        Subclass from Menu class.

        :param game: (Game [game.py]) Main Game object.
        """
        Menu.__init__(self, game)
        self.state = 'Start' # which menu part is selected
        self.startx, self.starty = self.mid_w, self.mid_h + 35
        self.optionx, self.optiony = self.mid_w, self.mid_h + 70
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 105
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty) # cursor position in the start of the game
        self.banner =  pygame.image.load('images/menu_finish_bar.jpg')
        self.background = pygame.image.load('images/fons.jpg')

    def display_menu(self):
        """
        Displays menu.
        Main menu loop.
        """
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.background, (75, 0))
            self.game.draw_text('Tūrisma rallijs Liepāja 2022', 50, self.mid_w, self.mid_h - 100)
            self.game.draw_text('Sākt spēli', 35, self.startx, self.starty)
            self.game.draw_text('Iestatījumi', 35, self.optionx, self.optiony)
            self.game.draw_text('Par spēli', 35, self.creditsx, self.creditsy)
            self.game.display.blit(self.banner, (0, 0))
            self.game.display.blit(self.banner, (self.game.DISPLAY_W - 75, 0))
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        """
        Listens for the keyboard event (keys pressed) and moves cursor (*) accordingly.
        """
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionx + self.offset, self.optiony)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits' # Credits = About game
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'  # Credits = About game
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionx + self.offset, self.optiony)
                self.state = 'Options'

    def check_input(self):
        """
        Listens for keyboard events and changes Menu.state state.
        """
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        """
        Initialize OptionsMenu object.
        Subclass from Menu class.

        :param game: (Game [game.py]) Main Game object.
        """
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 35
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        """
        Displays menu.
        Main menu loop.
        """
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Iestatījumi', 50, self.mid_w, self.mid_h - 50)
            self.game.draw_text('Skaņa', 35, self.volx, self.voly)
            self.game.draw_text('Kontrole', 35, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        """
        Listens for keyboard events and changes Menu.state state.
        """
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TODO: Create a Volume menu and a Controls menu
            pass

def CreditsMenu(Menu):
    def __init__(self, game):
        """
        Initialize CreditsMenu object.
        Subclass from Menu class.

        :param game: (Game [game.py]) Main Game object.
        """
        Menu.__init__(self.game)

    def display_menu(self):
        """
        Displays menu.
        Main menu loop.
        """
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Par spēli', 50, self.mid_w, self.mid_h - 50)
            self.game.draw_text('Spēli izveidoja komanda "Fire in the server room"', 35, self.mid_w, self.mid_h + 35)
            self.game.draw_text('- Veronika Lohmanova', 25, self.mid_w, self.mid_h + 60)
            self.game.draw_text('- Ramona Poreitere', 25, self.mid_w, self.mid_h + 85)
            self.game.draw_text('- Aleksandrs Vjaters', 25, self.mid_w, self.mid_h + 110)
            self.blit_screen()













