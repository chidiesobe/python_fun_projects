from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from generator import generate_password


app = FastAPI(title="Ceed Media Password Generator API")

class PasswordResponse(BaseModel):
    password: str
    

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Ceed Media Password Generator API"}

@app.get("/generate", response_model=PasswordResponse, tags=["Generate"])
def generate(length: int = Query(12, ge=5, le=64), include_upper:bool = Query(True), include_digits: bool = Query(True),
             include_special: bool = Query(False)):
    try: 
        pwd = generate_password(length, include_upper, include_digits, include_special)
        return {"password": pwd}
    except ValueError as e: 
        raise HTTPException(status_code=400, detail={e})