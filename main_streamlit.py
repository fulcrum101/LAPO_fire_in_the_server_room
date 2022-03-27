import streamlit as st
import firebase_admin
from firebase_admin import db
import pandas as pd
import json
def main():
    st.set_page_config(
        page_title="E-Avīze",
        page_icon="🧊"
    )

    st.title('Tūrisma rallijs Liepāja 2022')
    st.caption('Tūrisma rallijs Liepāja 2022')
    cred_obj = firebase_admin.credentials.Certificate('leaderboard_database/lapoleaderboard-firebase-adminsdk-shvog-0e31c6bc10.json')
    default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': 'https://lapoleaderboard-default-rtdb.europe-west1.firebasedatabase.app/'})
    results = db.reference('/').get()
    list = []
    for x in results:
        list.append(json.loads(results[x]))
    df = pd.DataFrame(list)
    df = df.sort_values(by=['points'])
    st.dataframe(df)

if __name__ == "__main__":
    main()