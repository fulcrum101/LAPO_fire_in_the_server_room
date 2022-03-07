import pygame
import json 

#some of the needed functions for map
#map = Map(self)
#map.blit_screen()
#map.get_points()
#map.draw_points(4, (0,0,0), (225,0,0))

class Map():
    def __init__(self, game):
        self.game = game
        self.width, self.height = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.pixelWidth, self.pixelHeight = 5, 5 # where do i get this from???
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 45, 45) # x, y, width, height
        self.background = pygame.image.load("images\map\base-map.png")
        self.latitudeMin = 55.5
        self.latitudeMax = 57.9
        self.longitudeMin = 20.0
        self.longitudeMax = 25.0

    def blit_screen(self):
        self.game.window.blit(self.background, (0, 0))
        pygame.display.update()  # flush
    
    def getPointData(self, filePath):
        file = open(filePath, "r") #loads and reads the json file
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

    #run once in the beginning
    def get_points(self, pathToDataSource): #path ="data-sources/points.json"
        self.pointCoordinatesX, self.pointCoordinatesY, self.roads = self.getPointData(pathToDataSource)
        #self.cityCoordinatesX, ... # do the same thing when cities.json file added
        self.pointStates=[0]*len(self.pointCoordinatesX)

    #draws a square - will be used to mark points and cities on the map
    def draw_a_square(self, nInGamePixels, x, y, colour):
        pygame.draw.rect(self.game.window, colour, (x*self.pixelWidth, y*self.pixelHeight, self.pixelWidth*nInGamePixels, self.pixelHeight*nInGamePixels))
        self.blit_screen() 

    #marks points and cities on the map
    def draw_points(self, nInGamePixels, colourIfNotVisited, colourIfVisited):
        id = 0
        for state in self.pointStates:
            if state == 0: #not visited
                self.draw_a_square(nInGamePixels, self.pointCoordinatesX[id], self.pointCoordinatesY[id], colourIfNotVisited)#draw in one colour
            else:
                self.draw_a_square(nInGamePixels, self.pointCoordinatesX[id], self.pointCoordinatesY[id], colourIfVisited)#draw in a different colour
            id+=1

    def draw_a_road(self, x1, y1, x2, y2, linewidth, colour):
        startGeometry = ((int)((x1+2.5)*self.pixelWidth), (int)((y1+2.5)*self.pixelHeight))
        endGeometry = ((int)((x2+2.5)*self.pixelWidth), (int)((y2+2.5)*self.pixelHeight))
        pygame.draw.line(self.window, colour, startGeometry, endGeometry, linewidth)
        self.blit_screen()

    def draw_roads(self, lineWidth, colour):
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
