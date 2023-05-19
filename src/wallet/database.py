from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings

engine = create_engine(
    settings.database_url,
    connect_args={'check_same_thread': False},
)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)


def get_session():
    with Session() as session:
        yield session
