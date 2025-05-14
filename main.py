from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers import user_router
from utils.init_db import create_table


# alternate of startup event(deprecated).
@asynccontextmanager
async def lifespan(app:FastAPI):
    create_table()
    print("database created!")
    yield
    print("Application is shut down.")

    
app =FastAPI(lifespan=lifespan)


app.include_router(user_router.router)