from sqlalchemy.orm import Session
from . import models, schemas

# Create
def create_asset(db: Session, asset: schemas.AssetCreate):
    db_asset = models.Asset(
        name=asset.name,
        cost=asset.cost,
        purchase_date=asset.purchase_date,
        useful_life=asset.useful_life
    )
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

# Read
def get_asset(db: Session, asset_id: int):
    return db.query(models.Asset).filter(models.Asset.id == asset_id).first()

def get_assets(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Asset).offset(skip).limit(limit).all()

# Update
def update_asset(db: Session, asset_id: int, asset_update: schemas.AssetUpdate):
    db_asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if db_asset is None:
        return None
    for key, value in asset_update.dict(exclude_unset=True).items():
        setattr(db_asset, key, value)
    db.commit()
    db.refresh(db_asset)
    return db_asset

# Delete
def delete_asset(db: Session, asset_id: int):
    db_asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if db_asset is None:
        return None
    db.delete(db_asset)
    db.commit()
    return db_asset
