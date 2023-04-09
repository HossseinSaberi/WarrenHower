from fastapi import FastAPI
from Users.routers import router as user_router
app = FastAPI()
app.include_router(user_router , tags=['Users'])