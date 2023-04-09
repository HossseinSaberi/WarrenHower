from pydantic import BaseModel

class BaseUser(BaseModel):
    username : str
    
    class Config:
        orm_mode = True
        
class UserResponseList(BaseUser):
    uid :int