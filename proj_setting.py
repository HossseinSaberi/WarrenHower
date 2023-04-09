from pydantic import BaseSettings , Field

class Settings(BaseSettings):
    db_ip : str 
    db_port : str
    db_name : str
    db_username : str
    db_password : str
    host : str
    port : str
    reload : bool
    
    class Config:
        env_file = ".env"
        
settings = Settings()
 