import pytest

from src.settings.base import Base, engine, SessionLocal
from src.settings.config import settings


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    assert settings.MODE == 'TEST'
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

@pytest.fixture()
def db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()