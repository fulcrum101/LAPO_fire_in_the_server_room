n={
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "properties": {
          "name": "Liepāja",
          "id": 0,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            21.01107895374298,
            56.508205438199695
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Rīga",
          "id": 1,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            24.11383956670761,
            56.95182914718994
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Jūrmala",
          "id": 2,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            23.77570152282715,
            56.96967306284926
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Jelgava",
          "id": 3,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            23.732807636260986,
            56.65403266197735
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Biržai",
          "id": 4,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            24.756531715393066,
            56.20159557922729
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Panevėžys",
          "id": 5,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            24.355702400207516,
            55.730928305992435
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Šiauliai",
          "id": 6,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            23.336685597896576,
            55.92708487695348
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Telšiai",
          "id": 7,
          "roads": ""
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            22.249503135681152,
            55.98449506249372
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Klaipėda",
          "id": 8,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            21.133100017905235,
            55.71044064366295
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Palanga",
          "id": 9,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            21.071471571922302,
            55.91737771650334
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Pāvilosta",
          "id": 10,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            21.172547936439514,
            56.88922168362694
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Ventspils",
          "id": 11,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            21.56363010406494,
            57.38963995827247
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Kolka",
          "id": 12,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            22.58812665939331,
            57.74496700516343
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Talsi",
          "id": 13,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            22.59379416704178,
            57.243874051658466
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Kuldīga",
          "id": 14,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            21.96886897087097,
            56.96969645526097
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Skrunda",
          "id": 15,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            22.01513171195984,
            56.67597702134641
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Mažeikiai",
          "id": 16,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            22.348251342773438,
            56.31096687405081
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Tukums",
          "id": 17,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            23.190186023712158,
            56.966819078403816
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "name": "Saldus",
          "id": 18,
          "roads": []
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            22.493053078651428,
            56.66570803870003
          ]
        }
      }
    ]
  }
import sqlite3
con = sqlite3.connect('cities.db')
cur = con.cursor()
for i in n["features"]:
    cur.execute(f'INSERT INTO Points VALUES ("{i["properties"]["name"]}",{i["geometry"]["coordinates"][0]},{i["geometry"]["coordinates"][1]});')
con.commit()
con.close()
