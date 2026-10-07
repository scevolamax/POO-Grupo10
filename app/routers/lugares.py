from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/lugares", tags=["Lugares"])

@router.post("/", response_model=schemas.LugarResponse)
def crear_lugar(lugar: schemas.LugarCreate, db: Session = Depends(get_db)):
    db_lugar = models.Lugar(**lugar.model_dump())
    db.add(db_lugar)
    db.commit()
    db.refresh(db_lugar)
    return db_lugar

@router.get("/", response_model=List[schemas.LugarResponse])
def listar_lugares(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Lugar).offset(skip).limit(limit).all()