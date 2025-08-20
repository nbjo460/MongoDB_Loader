import os
import json
from bson import json_util
from pymongo import MongoClient
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


    def create_data_first_time(self):
        first_soldier = Soldier( "12","moshe", "shulman", "+vdvffd", "4")
        try:
            self.insert_soldier(first_soldier)
            print("first added")
        except:
            pass

    @connection
    def insert_soldier(self, collection, soldier : Soldier):
        collection.insert_one(soldier.to_dict())
        print("Added one")

    @connection
    def load_data(self, collection):
        people = list(collection.find())
        result = json.loads(json_util.dumps(people))
        print("loaded")
        return result

    @connection
    def delete_soldier(self, collection, _id):
        if collection.find_one({"_id":_id}):
            collection.delete_one({"_id":_id})
            return "Deleted"
        return "Deletion failed"

    @connection
    def update_soldier(self, collection, _id, parameters : dict):
        result = collection.updateOne({"_id":_id},{"$set":parameters})
        if result.modified_count > 0: return "Success"
        else: return "Failed to update"