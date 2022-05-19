from typing import List
from fastapi import APIRouter, Body, Depends
from starlette.status import HTTP_201_CREATED

from app.models.users import UserCreate, UserPublic
from app.db.repositories.users import UsersRepository
from app.api.dependencies.database import get_repository

router = APIRouter()


@router.get("")
async def get_all_users() -> List[dict]:
    users = [
        {"id": 1, "name": "hansol"},
        {"id": 2, "name": "dudu"}
    ]
    return users


@router.post("/", response_model=UserPublic, name="user:create-user", status_code=HTTP_201_CREATED)
async def create_new_user(
    new_user: UserCreate = Body(..., embed=True),
    user_repo: UsersRepository = Depends(get_repository(UsersRepository)),
) -> UserPublic:
    created_user = await user_repo.create_user(new_user=new_user)
    return created_user