from sqlalchemy import Column , Integer , String , Boolean , ForeignKey
from sqlalchemy.orm import relationship , column_property
from database import Base


class Users(Base):
    __tablename__ = 'users'
    
    uid = Column(Integer , autoincrement=True , primary_key=True , index=True)
    email = Column(String , index=True , unique=True , nullable=False)
    username = Column(String , index=True , unique=True , nullable=False)
    password = Column(String , nullable=False)
    is_active = Column(Boolean , default=False)
    profile = relationship('Profile' , back_populates='user',uselist=False)
    
    def __repr__(self) -> str:
        return self.username
    
class Profile(Base):
    __tablename__ = 'users_profile'
    
    uid = Column(Integer , autoincrement=True , primary_key=True , index=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    age = Column(Integer)
    gender = Column(String)
    user_id = Column(Integer , ForeignKey('users.uid') , nullable=True)
    user = relationship('Users' , back_populates='profile')
    fullname = column_property(firstname+" "+lastname)
    
    def __repr__(self) -> str:
        return self.fullname