from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def get_all_users() -> List[dict]:
    users = [
        {"id": 1, "name": "hansol"},
        {"id": 2, "name": "dudu"}
    ]
    return users
