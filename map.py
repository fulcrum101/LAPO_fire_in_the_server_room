from operator import ne
import pygame
import json 
from quizz import Quizz

class Map():
    def __init__(self, game):
        """
        Initialize Map object.

        :param game: (Game [game.py]) Main Game object.
        """
        self.idToI ={}
        self.game = game
        self.width, self.height = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.pixelWidth, self.pixelHeight = 5, 5 # where do i get this from???
        self.running = self.game.map_running
        self.cursor_rect = pygame.Rect(0, 0, 45, 45) # x, y, width, height
        self.latitudeMin = 55.5
        self.latitudeMax = 57.9
        self.longitudeMin = 20.0
        self.longitudeMax = 25.0
        self.selectedI = -1
        self.selectedMommyI = -1
        self.unvisitedLeft = 0
        self.baseSurface = pygame.image.load("images/map/base-map.png")
        self.get_points("data-sources/points-and-stations-connected.json")
        self.startPointId = 53
        self.endPointId = 54
        

    def blit_screen(self):
        """
        Resets screen.
        """
        self.game.display.blit(self.baseSurface, (0,0))
        self.draw_points(4, self.game.SKYBLUE, self.game.BLUE, self.game.MAGENTA, self.game.RED, self.game.YELLOW)
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()  # flush
    
    def display_map(self):
        """
        Displays map.
        """
        #self.draw_points(4, self.game.MAGENTA, self.game.MAGENTA)
        self.running = True
        while self.running:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.running = False
                self.game.curr_menu = self.game.credits

            self.blit_screen()
            self.check_input()
    
    def check_input(self):
        """
        Listens for keyboard events and changes Menu.state state.
        """
        #self.move_cursor()
        if self.game.START_KEY:
            self.game.START_KEY=False
            self.game.activePointI = self.selectedI
            self.selectedMommyI = self.selectedI
            self.game.START_KEY=False
            if self.visiteds[self.selectedI]==0:
                self.running = False
                self.game.activeQuizzDone=0
                self.game.quizz.ControlPointQuizz(self.ids[self.selectedI])
                self.unvisitedLeft = self.unvisitedLeft-1
                self.visiteds[self.selectedMommyI] = 1
                self.makeAvailable(self.selectedMommyI)
                self.game.activeRaceDone=0
                self.running = True
                
            self.game.START_KEY=False
        if self.game.RIGHT_KEY:
            self.moveSelected(1)
            self.game.RIGHT_KEY = False
        if self.game.LEFT_KEY:
            self.moveSelected(-1)
            self.game.LEFT_KEY = False

    def moveSelected(self, direction):
        newI = 0
        neiI = 0
        found = 0
        for neighbour in self.roads[self.selectedMommyI]:
            if((int)(neighbour)==(int)(self.endPointId)):
                neiI = neiI+1
                continue
            if((int)(neighbour)==(int)(self.ids[self.selectedI])):
                found = 1
                break
            neiI=neiI+1
        neiI = (neiI + +direction+len(self.roads[self.selectedMommyI]) ) % len(self.roads[self.selectedMommyI])
        if (int)(self.roads[self.selectedMommyI][neiI])==(int)(self.endPointId):
            neiI = (neiI + +direction+len(self.roads[self.selectedMommyI]) ) % len(self.roads[self.selectedMommyI])
        newI = self.idToI.get((int)(self.roads[self.selectedMommyI][neiI]))
        self.selectedI = newI
        print("SELECTED : " + str(self.selectedI))

    def makeAvailable(self, momI):
        for child in self.roads[momI]:
            if(child==self.endPointId):
                if(self.unvisitedLeft>1):
                    continue
            childI = (int)(self.idToI.get((int)(child)))
            self.availables[childI]=1

    def getPointData(self, filePath):
        """
        Reads point data from file.

        :param filePath: (str) Path of file to read.
        :return: coordinatesX, coordinatesY, roads
        - coordinatesX: ([]*int) X coordinates of the points.
        - coordinatesY: ([]*int) Y coordinates of the points.
        - roads: ([]*[]*int) list of neighbour points of the points.
        """
        file = open(filePath, "r", encoding="utf8") #loads and reads the json file
        content = file.read()
        data = json.loads(content)
        nOfPixelsX = self.width/self.pixelWidth
        nOfPixelsY = self.height/self.pixelHeight
        widthInCoordinates = self.longitudeMax-self.longitudeMin
        heightInCoordinates = self.latitudeMax-self.latitudeMin
        coordinatesX=[] #coordinate list initialisation
        coordinatesY=[]
        names = []
        ids = []
        types = []
        roads = []
        availables = []
        visiteds = []
        i = 0
        for point in data['features']:
            x = (int)((point['geometry']['coordinates'][0]-self.longitudeMin)/widthInCoordinates*self.width/self.pixelWidth)
            coordinatesX.append((int)(x))
            y = nOfPixelsY-(int)((point['geometry']['coordinates'][1]-self.latitudeMin)/heightInCoordinates*self.height/self.pixelHeight)
            coordinatesY.append((int)(y))
            roadstring = str(point['properties']['roads'])
            roadlist = list(roadstring.split(" "))
            roadlist.pop()
            roads.append(roadlist)
            typee = point['properties']["type"]
            types.append(typee)
            if(typee == "Point"): self.unvisitedLeft = self.unvisitedLeft+1
            id = (int)(point['properties']['id'])
            ids.append(id)
            self.idToI[id]=i
            if(id == 53): 
                availables.append(1)
                self.selectedI = i
            else :
                availables.append(0)
            visiteds.append(0)
            name = point['properties']['name']
            names.append(name)
            i=i+1
        return coordinatesX, coordinatesY, roads, types, availables, visiteds, names, ids

    def get_points(self, pathToDataSource): # path= "data-sources/points.json" or "data-sources/cities.json"
        """
        Loads in all points data.
        !!! Run once in the beginning

        :param pathToDataSource: (str) Path to file (.json) with all points. 
        """
        self.pointCoordinatesX, self.pointCoordinatesY, self.roads, self.types, self.availables, self.visiteds, self.names, self.ids = self.getPointData(pathToDataSource)
        #self.cityCoordinatesX, ... # do the same thing when cities.json file added
        self.pointStates=[0]*len(self.pointCoordinatesX)

    def draw_a_square(self, nInGamePixels, x, y, colour):
        """
        Draws a square.
        Used to mark points and cities on the map.

        :param nInGamePixels: (int) Number of pixels of the window/screen.?
        :param x: (int) X coordinate of the rect.
        :param y: (int) Y coordinate of the rect.
        :param colour: (turple (z, z, z)) Color of the rect.
        """
        pygame.draw.rect(self.game.display, colour, (x*self.pixelWidth, y*self.pixelHeight, self.pixelWidth*nInGamePixels, self.pixelHeight*nInGamePixels))
        #self.blit_screen() 

    def draw_points(self, nInGamePixels, colourIfNotVisitedStation, colourIfVisitedStation, colourIfNotVisitedPoint, colourIfVisitedPoint, colourSelected):
        """
        Marks points and cities on the map.

        :param nInGamePixels: (int) Number of pixels of the window/screen.?
        :param colourIfNotVisited: (turple (z, z, z)) Color of the point if it was not previously visited.
        :param colourIfVisited: (turple (z, z, z)) Color of the point if it was not previously visited.
        """
        i = -1
        for state in self.visiteds:
            i+=1
            if self.availables[i]==0:
                continue
            if self.selectedI == i:
                self.draw_a_square(nInGamePixels, self.pointCoordinatesX[i], self.pointCoordinatesY[i], colourSelected)#draw in one colour
                continue
        
            if self.types[i]=="chargingStation":
                if state == 0: #not visited
                    self.draw_a_square(nInGamePixels, self.pointCoordinatesX[i], self.pointCoordinatesY[i], colourIfNotVisitedStation)#draw in one colour
                else:
                    self.draw_a_square(nInGamePixels, self.pointCoordinatesX[i], self.pointCoordinatesY[i], colourIfVisitedStation)#draw in a different colour
            else:
                if state == 0: #not visited
                    self.draw_a_square(nInGamePixels, self.pointCoordinatesX[i], self.pointCoordinatesY[i], colourIfNotVisitedPoint)#draw in one colour
                else:
                    self.draw_a_square(nInGamePixels, self.pointCoordinatesX[i], self.pointCoordinatesY[i], colourIfVisitedPoint)#draw in a different colour
            
            

    def draw_a_road(self, x1, y1, x2, y2, linewidth, colour):
        """
        Draws road (line).

        :param x1: (int) X coordinate of start.
        :param y1: (int) Y coordinate of start.
        :param x2: (int) X coordinate of end.
        :param y2: (int) Y coordinate of end.
        :param linewidth: (int) Width of the line.
        :param colour: (turple (z, z, z)) Color of the line.
        """
        startGeometry = ((int)((x1+2.5)*self.pixelWidth), (int)((y1+2.5)*self.pixelHeight))
        endGeometry = ((int)((x2+2.5)*self.pixelWidth), (int)((y2+2.5)*self.pixelHeight))
        pygame.draw.line(self.window, colour, startGeometry, endGeometry, linewidth)
        self.blit_screen()

    def draw_roads(self, lineWidth, colour):
        """
        Iterates trough all roads from Map.roads and draws them with Map.draw_a_road().

        :param linewidth: (int) Width of the line.
        :param colour: (turple (z, z, z)) Color of the line.
        """
        id = 0
        for state in self.pointStates:
            x1 = self.pointCoordinatesX[id]
            y1 = self.pointCoordinatesY[id]
            for destination in self.roads[id]:
                x2 = self.pointCoordinatesX[destination]
                y2 = self.pointCoordinatesY[destination]
                print("drawing.. "+(str)(x1) + " " + (str)(y1) + "\nto.. "+(str)(x2) + " "+(str)(y2))
                self.draw_a_road(x1, y1, x2, y2, lineWidth, colour)
            id+=1
