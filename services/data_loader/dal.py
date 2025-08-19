import json
from bson import json_util
from pymongo import MongoClient
import os


def connection(func):
    def wrapper(self, *args, **kwargs):
        try:
            client = MongoClient(self.URI)
            print("opened")
            result = func(self, client, *args, **kwargs)
            client.close()
            print("closed")
            return result
        except Exception as e:
            print(f"Exception: {e}")
    return wrapper


class Dal:
    def __init__(self):
        host = os.getenv("HOST")
        user = os.getenv("USER")
        password = os.getenv("PASSWORD")
        self.URI = f"mongodb://{user}:{password}@{host}/"
        self.create_data_first_time()
    @connection
    def create_data_first_time(self, client):
        db = client.menachem
        data = db.data
        data.insert_one({"_id":1, "first name": "menachem", "last name":"yarhi"})
        print("added")
    @connection
    def load_data(self, client):
        db = client.menachem
        data = db.data
        people = list(data.find())
        return json.loads(json_util.dumps(people))


    # def connection(self):
    #     client = MongoClient(self.URI)
