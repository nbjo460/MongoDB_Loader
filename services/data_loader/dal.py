import json
from bson import json_util
from pymongo import MongoClient
import os

from soldier import Soldier


def connection(func):
    def wrapper(self, *args, **kwargs):
        client = None
        try:
            client = MongoClient(self.URI)
            print("opened")
            db = client.enemy_silodier
            collection = db.soldier_details
            result = func(self, collection, *args, **kwargs)
            return result
        except Exception as e:
            print(f"Exception: {e}")
        finally:
            try:
                client.close()
                print("closed")
            except Exception as e:
                print("Can't close ", e)

    return wrapper


class Dal:
    def __init__(self):
        host = os.getenv("HOST")
        user = os.getenv("USER")
        password = os.getenv("PASSWORD")
        self.URI = f"mongodb://{user}:{password}@{host}/"
        self.create_data_first_time()

    @connection
    def create_data_first_time(self, collection):
        first_soldier = Soldier( "moshe", "shulman", "+vdvffd", "4")
        self.insert_one_soldier(first_soldier, collection)
        print("first added")

    @staticmethod
    def insert_one_soldier(soldier : Soldier, collection):
        collection.insert_one(soldier.to_dict())
        print("Added one")

    @connection
    def load_data(self, collection):
        people = list(collection.find())
        result = json.loads(json_util.dumps(people))
        print("loaded")
        return result
