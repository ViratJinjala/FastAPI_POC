

from typing import Annotated
from fastapi import APIRouter, Depends, status

from config.database import get_db
from schemas.user_schema import UserInput, UserOutput
from sqlalchemy.orm import Session

from service.user_service import UserService


router = APIRouter(prefix="/users", tags=["Users"])

DB_Dependency = Annotated[Session,Depends(get_db)]



@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserOutput)
async def create_user(user: UserInput, db: DB_Dependency):
    service = UserService(db)
    return service.create(user)