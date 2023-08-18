from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext

DB_URL = "sqlite:///./app.db"

engine = create_engine(
    DB_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Get the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Hash user password before storing to db
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password):
    return pwd_context.hash(password)


def verify_password(user_password, hashed_password):
    return pwd_context.verify(user_password, hashed_password)
