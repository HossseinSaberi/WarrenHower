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
    jwt_secret_key :str
    jwt_algorithm : str
    jwt_access_token_expire_minutes : int
    
    class Config:
        env_file = ".env"
        
settings = Settings()
 