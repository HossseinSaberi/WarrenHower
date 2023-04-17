from pydantic import BaseModel

"""
    profile schemas
"""


class BaseProfile(BaseModel):
    fullname: str
    gender: str

    class Config:
        orm_mode = True


class Profile(BaseProfile):
    firstname: str
    lastname: str
    age: int


class ProfileResponse(Profile):
    pid: int


"""
    user schemas
"""
class BaseUser(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class UserResponseList(BaseUser):
    uid: int


class UserCreation(BaseUser):
    password: str


class UserEdition(UserCreation):
    pass 

class UserDetails(UserResponseList):
    profile: ProfileResponse | None
