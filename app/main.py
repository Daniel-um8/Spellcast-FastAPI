from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para obtener sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Bienvenido a Spellcast API"}
