from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class Asset(Base):
    __tablename__ = 'assets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    purchase_date = Column(Date)
    purchase_price = Column(Float)
    useful_life = Column(Integer)
    asset_class = Column(Integer)


