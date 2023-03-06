
# pydantic의 model

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    email: str
    is_active: bool

    class Config: # pydantic이 Alchemy model을 사용할 수 있도록 설정
        orm_mode = True