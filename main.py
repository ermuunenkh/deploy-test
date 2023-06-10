from fastapi import FastAPI

app = FastAPI()

@app.get("/data")
async def read_data():
    return {"message": "Hello, world from FastAPI!"}
