from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL =""

engine = create_engine()
SessionLocal = sessionmaker()
Base = declarative_base()
