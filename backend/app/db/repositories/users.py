from app.db.repositories.base import BaseRepository
from app.models.users import UserCreate, UserUpdate, UserInDB


CREATE_USER_QUERY = """
    INSERT INTO users (name)
    VALUES (:name)
    RETURNING id, name;
"""


class UsersRepository(BaseRepository):
    """"
    All database actions associated with the user resource
    """

    async def create_user(self, *, new_user: UserCreate) -> UserInDB:
        query_values = new_user.dict()
        user = await self.db.fetch_one(query=CREATE_USER_QUERY, values=query_values)

        return UserInDB(**user)

