from app.db.repositories.base import BaseRepository
from app.models.users import UserCreate, UserUpdate, UserInDB


CREATE_USER_QUERY = """
    INSERT INTO users (name)
    VALUES (:name)
    RETURNING id, name;
"""

GET_USER_BY_ID_QUERY = """
    SELECT id, name
    FROM users
    WHERE id = :id;
"""



class UsersRepository(BaseRepository):
    """"
    All database actions associated with the user resource
    """

    async def create_user(self, *, new_user: UserCreate) -> UserInDB:
        query_values = new_user.dict()
        user = await self.db.fetch_one(query=CREATE_USER_QUERY, values=query_values)

        return UserInDB(**user)

    async def get_user_by_id(self, *, id: int) -> UserInDB:
        user = await self.db.fetch_one(query=GET_USER_BY_ID_QUERY, values={"id": id})
        if not user:
            return None
        return UserInDB(**user)

