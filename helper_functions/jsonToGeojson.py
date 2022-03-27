import json 

#parameters:
width = 1000
height = 1000
pixelWidth = 5
pixelHeight = 5
#these are the real-life corner coordinates of the map
latitudeMin = 55.5
latitudeMax = 57.9
longitudeMin = 20.0
longitudeMax = 25.0
latitudeNames = ["latitude", "latitude"]
longitudeNames = ["longitude", "longitude"]
nameNames = ["label", "name"]
pathToFiles = ["one/all-stations.json", "one/lietuva-stations.json"]
pathToResultFiles = ["all-stations-clean.json", "lt-stations-clean.json"]
#nOfPoints=data['features'].length
def getPointCoordinates(filePath, latitudeName, longitudeName, nameName, pathtoclean, featureType, startId):
    file = open(filePath, "r", encoding="utf8") #loads and reads the json file
    content = file.read()
    data = json.loads(content)
    newdata={}
    features=[]
    i = 0
    id = startId
    for point in data['features']:
        feature={}
        feature["type"] = "Feature"
        properties={}
        properties["name"] = point[nameName]
        properties["id"] = id
        id=id+1
        properties["roads"] = []
        properties["type"] = featureType
        feature["properties"] = properties
        geometry ={}
        geometry["type"] = "Point"
        geometry["coordinates"] = [point[longitudeName], point[latitudeName]]
        feature["geometry"] = geometry
        features.append(feature)
    newdata["type"] = "FeatureCollection"
    newdata["features"] = features
    with open(pathtoclean, "w", encoding="utf8") as f:
        json.dump(newdata, f, indent=2, ensure_ascii=False)

getPointCoordinates(pathToFiles[0], latitudeNames[0], longitudeNames[0], nameNames[0], pathToResultFiles[0], "chargingStation", 0)
getPointCoordinates(pathToFiles[1], latitudeNames[1], longitudeNames[1], nameNames[1], pathToResultFiles[1], "chargingStation", 264)

