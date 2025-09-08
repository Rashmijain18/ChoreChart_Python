from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# This tells your app how to connect to the database
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:adminpass@postgres:5432/chorechart_python")

# Create the database engine (like a connection manager)
engine = create_engine(
    DATABASE_URL,
    echo=True,  # This shows SQL commands in your logs (helpful for learning)
    pool_pre_ping=True,
    pool_recycle=300
)

# Create a session factory (like a template for database sessions)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for models
Base = declarative_base()

# This function gives you a database session when you need it
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()