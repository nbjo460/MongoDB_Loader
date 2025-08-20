import fastapi
from dal import Dal

app = fastapi.FastAPI()

dal = Dal()

@app.get("/")
def root():
    return {}
@app.get("/load")
def load_db():
    return dal.load_data()
