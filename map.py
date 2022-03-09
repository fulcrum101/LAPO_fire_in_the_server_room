import pygame
import json 

#some of the needed functions for map
#map = Map(self)
#map.blit_screen()
#map.get_points()
#map.draw_points(4, (0,0,0), (225,0,0))

class Map():
    def __init__(self, game):
        """
        Initialize Map object.

        :param game: (Game [game.py]) Main Game object.
        """
        self.game = game
        self.width, self.height = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.pixelWidth, self.pixelHeight = 5, 5 # where do i get this from???
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 45, 45) # x, y, width, height
        baseSurface = pygame.image.load("images/map/base-map.png")
        self.latitudeMin = 55.5
        self.latitudeMax = 57.9
        self.longitudeMin = 20.0
        self.longitudeMax = 25.0

    def blit_screen(self):
        """
        Resets screen.
        """
        self.game.window.blit(self.baseSurface, (0,0))
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()  # flush
    
    def getPointData(self, filePath):
        """
        Reads point data from file.

        :param filePath: (str) Path of file to read.
        :return: coordinatesX, coordinatesY, roads
        - coordinatesX: (int) X coordinate of the point.
        - coordinatesY: (int) Y coordinate of the points.
        - roads: ([]) list of points connected.
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
        roads = []
        for point in data['features']:
            x = (int)((point['geometry']['coordinates'][0]-self.longitudeMin)/widthInCoordinates*self.width/self.pixelWidth)
            coordinatesX.append((int)(x))
            y = nOfPixelsY-(int)((point['geometry']['coordinates'][1]-self.latitudeMin)/heightInCoordinates*self.height/self.pixelHeight)
            coordinatesY.append((int)(y))
            roadlist = point['properties']['roads']
            roads.append(roadlist)
            #can read name of point and id as well
        return coordinatesX, coordinatesY, roads

    def get_points(self, pathToDataSource): # path= "data-sources/points.json" or "data-sources/cities.json"
        """
        Loads in all points data.
        !!! Run once in the beginning

        :param pathToDataSource: (str) Path to file (.json) with all points. 
        """
        self.pointCoordinatesX, self.pointCoordinatesY, self.roads = self.getPointData(pathToDataSource)
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
        pygame.draw.rect(self.game.window, colour, (x*self.pixelWidth, y*self.pixelHeight, self.pixelWidth*nInGamePixels, self.pixelHeight*nInGamePixels))
        self.blit_screen() 

    def draw_points(self, nInGamePixels, colourIfNotVisited, colourIfVisited):
        """
        Marks points and cities on the map.

        :param nInGamePixels: (int) Number of pixels of the window/screen.?
        :param colourIfNotVisited: (turple (z, z, z)) Color of the point if it was not previously visited.
        :param colourIfVisited: (turple (z, z, z)) Color of the point if it was not previously visited.
        """
        id = 0
        for state in self.pointStates:
            if state == 0: #not visited
                self.draw_a_square(nInGamePixels, self.pointCoordinatesX[id], self.pointCoordinatesY[id], colourIfNotVisited)#draw in one colour
            else:
                self.draw_a_square(nInGamePixels, self.pointCoordinatesX[id], self.pointCoordinatesY[id], colourIfVisited)#draw in a different colour
            id+=1

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
