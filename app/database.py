from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# if you use docker, match the host with your db_container name
engine = create_engine("postgresql://postgres:admin@postgres:5432/law-lab4",
    echo=True
)

Base = declarative_base()

SessionLocal = sessionmaker(bind = engine)