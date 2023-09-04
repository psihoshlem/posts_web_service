from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from db_functions.db_config import user, host, password, db_name


engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@{host}/{db_name}", echo=False
)

Base = declarative_base()

class Post(Base):
    __tablename__ = "Posts"

    id_post = Column(Integer, primary_key=True)
    title = Column(String(55), nullable=False)
    text = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)