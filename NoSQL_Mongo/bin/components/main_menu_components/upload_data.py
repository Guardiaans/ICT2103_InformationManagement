import components.dbconnection as db
from datetime import datetime
import os
import inquirer as iq
import json
import pandas as pd


def uploadData():
#TODO: Implementing uploadData method
    try: 
        print("uploading data..")
        fileName = iq.text(message="Enter the directory of your file with your file name")
        df = pd.read_csv(fileName)
        data = df.to_dict(orient="records")
        print("data to be uploaded:")
        print(data)
        db.transactions.insert_many(data)
        print("Data uploaded to Mongo DB.")
    except:
        print("Failed to upload data.")
    return