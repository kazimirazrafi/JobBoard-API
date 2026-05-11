from sqlmodel import create_engine, Session
from ..core.config import settings

sqlite_url = f"sqlite:///data/{settings.DATABASE}"
engine = create_engine(sqlite_url)

def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()

