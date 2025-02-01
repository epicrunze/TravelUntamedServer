from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# Configure CORS settings
origins = [
    "*"  # Allow all origins. For production, specify your allowed origins, e.g., "https://example.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Allowed origins
    allow_credentials=True,
    allow_methods=["*"],             # Allow all HTTP methods
    allow_headers=["*"],             # Allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Hello, world! pog"}

@app.post("/api/data")
def receive_data(data: dict):
    return {"received": data}

@app.get("/api/test")
def receive_data():
    return {"message": "Hello, world! pog"}