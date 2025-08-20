import fastapi
from dal import Dal
from soldier import Soldier

app = fastapi.FastAPI()

dal = Dal()

@app.get("/")
def root():
    return {}
@app.get("/load")
def load_db():
    return dal.load_data()
@app.post("/add")
def add_soldier(parameters : dict = fastapi.Body(...)):
    dal.insert_soldier(Soldier(**parameters))
    return "good"
@app.delete("/delete/{soldier_id}")
def delete_soldier(soldier_id:int):
    dal.delete_soldier(soldier_id)
    return "deleted"
@app.put("/update/{soldier_id}")
def update_soldier(soldier_id : int, parameters : dict = fastapi.Body(...)):
    dal.update_soldier(soldier_id, parameters)
    return "updated"