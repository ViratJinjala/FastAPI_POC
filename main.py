from fastapi import FastAPI
from routers import user_router, todo_router, auth_router
# from contextlib import asynccontextmanager
# from utils.init_db import create_table



# We don't need to use this as we are using alembic


# @asynccontextmanager
# async def lifespan(app:FastAPI):
# create_table()
#     print("database created!")
#     yield
#     print("Application is shut down.")  
# app =FastAPI(lifespan=lifespan)

app = FastAPI()

app.include_router(user_router.router)
app.include_router(todo_router.router)
app.include_router(auth_router.router)