import fastapi
from dal import Dal
# import dal

app = fastapi.FastAPI()

dal = Dal()

@app.get("/load")
def load_db():
    pass
#  mongodb://root:12345@mongodb-community-server:27017/