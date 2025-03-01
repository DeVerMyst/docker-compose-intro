
from fastapi import FastAPI
import os

app = FastAPI()

API_URL = os.environ.get("API_URL")
API_PORT = int(os.environ.get("API_PORT"))

@app.get("/")
def read_root():
    return {"API URL": API_URL, "API PORT": API_PORT}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=API_URL, port=API_PORT)