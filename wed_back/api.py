from sqlalchemy.orm import Session

# from . import models, schemas
import models
import schemas


def get_claim(db: Session, slug: str):
    return db.query(models.Claim).filter(models.Claim.slug == slug).first()


def get_claims(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Claim).offset(skip).limit(limit).all()


def create_claim(db: Session, claim: schemas.Claim):
    db_claim = models.Claim(**claim.dict())
    db.add(db_claim)
    db.commit()
    db.refresh(db_claim)
    return db_claim

def update_claim(db: Session, claim: schemas.Claim):
    exist_claim = get_claim(db, claim.slug)
    data = claim.dict()
    if exist_claim:
        for k, v in data.items():
            setattr(exist_claim, k, v)
        db.commit()
        db.refresh(exist_claim)
        return exist_claim
    else:
        db_claim = models.Claim(**data)
        db.add(db_claim)
        db.commit()
        db.refresh(db_claim)
        return db_claim