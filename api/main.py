from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world! pog"}

@app.post("/api/data")
def receive_data(data: dict):
    return {"received": data}

@app.get("/api/test")
def receive_data():
    return {"message": "Hello, world! pog"}