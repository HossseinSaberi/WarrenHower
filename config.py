from fastapi import FastAPI
from Users.routers import router as user_router
from Authenticate.auth_api import router as jwt_router
app = FastAPI()
app.include_router(user_router , tags=['Users'] , prefix="/v1/Users",)
app.include_router(jwt_router , tags=['Token'] , prefix="/v1/Authenticate",)