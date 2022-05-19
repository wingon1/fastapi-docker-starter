from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

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


@router.get("/{id}/", response_model=UserPublic, name="users:get-user-by-id")
async def get_user_by_id(
  id: int, users_repo: UsersRepository = Depends(get_repository(UsersRepository))
) -> UserPublic:
    user = await users_repo.get_user_by_id(id=id)

    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No user found with that id.")

    return user



@router.post("/", response_model=UserPublic, name="user:create-user", status_code=HTTP_201_CREATED)
async def create_new_user(
    new_user: UserCreate = Body(..., embed=True),
    user_repo: UsersRepository = Depends(get_repository(UsersRepository)),
) -> UserPublic:
    created_user = await user_repo.create_user(new_user=new_user)
    return created_user