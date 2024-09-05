from fastapi import FastAPI
from database import Base
from database import SessionLocal
app = FastAPI()


@app.post("")
async def add_assets():
    pass

@app.get("")
async def get_assets():
    pass

@app.get("")
async def get_asset():
    pass
