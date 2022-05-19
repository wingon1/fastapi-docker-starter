import warnings
import os

import pytest
from async_asgi_testclient import TestClient

from fastapi import FastAPI
from databases import Database

from app.models.users import UserCreate, UserInDB
from app.db.repositories.users import UsersRepository

import alembic
from alembic.config import Config


# Apply migrations at beginning and end of testing session
@pytest.fixture(scope="session")
def apply_migrations():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    os.environ["TESTING"] = "1"
    config = Config("alembic.ini")

    alembic.command.upgrade(config, "head")
    yield
    alembic.command.downgrade(config, "base")


# Create a new application for testing
@pytest.fixture
def app(apply_migrations: None) -> FastAPI:
    from app.api.server import get_application

    return get_application()


# Grab a reference to our database when needed
@pytest.fixture
def db(app: FastAPI) -> Database:
    return app.state._db


@pytest.fixture
async def test_user(db: Database) -> UserInDB:
    user_repo = UsersRepository(db)
    new_user = UserCreate(
        name="test name",
    )
    return await user_repo.create_user(new_user=new_user)



# Make requests in our tests
@pytest.fixture
async def client(app: FastAPI) -> TestClient:
    async with TestClient(app) as client:
        yield client
