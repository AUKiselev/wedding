from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import api
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/claims/", response_model=schemas.Claim)
def create_claim(claim: schemas.Claim, db: Session = Depends(get_db)):
    db_claim = api.get_claim(db, slug=claim.slug)
    if db_claim:
        return api.update_claim(db=db, claim=claim)
    return api.create_claim(db=db, claim=claim)


@app.get("/claims/", response_model=list[schemas.Claim])
def read_claims(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    claims = api.get_claims(db, skip=skip, limit=limit)
    return claims


@app.get("/claims/{slug}", response_model=schemas.Claim)
def read_claim(slug: str, db: Session = Depends(get_db)):
    db_claim = api.get_claim(db, slug=slug)
    if db_claim is None:
        raise HTTPException(status_code=404, detail="Claim not found")
    return db_claim
