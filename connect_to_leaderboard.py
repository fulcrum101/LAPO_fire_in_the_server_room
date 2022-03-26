import firebase_admin
from firebase_admin import db
import json, os

def upload_result(name,  points, time):
    cred_obj = firebase_admin.credentials.Certificate('leaderboard_database/lapoleaderboard-firebase-adminsdk-shvog-0e31c6bc10.json')
    default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': 'https://lapoleaderboard-default-rtdb.europe-west1.firebasedatabase.app/'})
    ref = db.reference("/")
    res = {
        "name": name,
        "points": points,
        "time": time
    }
    json_object = json.dumps(res, indent=4)
    ref.set(json_object)
