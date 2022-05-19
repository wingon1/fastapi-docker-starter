from typing import Optional
from enum import Enum
from app.models.core import IDModelMixin, CoreModel


class UserBase(CoreModel):
    """
    All common characteristics of our Users resource
    """
    name: Optional[str]


class UserCreate(UserBase):
    name: str


class UserUpdate(UserBase):
    name: str


class UserInDB(IDModelMixin, UserBase):
    name: str


class UserPublic(IDModelMixin, UserBase):
    pass
