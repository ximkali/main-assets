from pydantic import BaseModel
from datetime import date

class AssetsBase(BaseModel):
    name:str
    coast:float
    purches_date:date
    usful_life:int
    asset_class:int

