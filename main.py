from fastapi import FastAPI
import db

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
    
@app.post("/a")
async def alpha_beta():
    return {"result": "success"}

@app.get("/get-customers")
async def get_customers():
    return db.get_customers()