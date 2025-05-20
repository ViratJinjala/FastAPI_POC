from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Body, Depends, status, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from dependancy.auth import get_current_user, get_current_admin_user
from models.user_model import User
from schemas.user_schema import UserInput, UserOutput, UserProfile
from service.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

DB_Dependancy = Annotated[Session, Depends(get_db)]

@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserOutput)
async def create_user(user: UserInput, db: DB_Dependancy):
    """
    user registration — no auth needed.
    """
    service = UserService(db)
    return service.create(user)

@router.get("/profile", response_model=UserProfile)
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user

@router.patch("/profile", response_model=UserProfile)
async def update_own_profile(
    db: DB_Dependancy,
    current_user: User = Depends(get_current_user),
    user_update: UserInput = Body(...),
):
    """
    Logged-in users can update their own profile.
    """
    service = UserService(db)
    updated_user = service.update_user(current_user.id, user_update)
    return updated_user

@router.get("", response_model=list[UserOutput])
async def get_all_users(
    db: DB_Dependancy, current_user: User = Depends(get_current_admin_user)
):
    """
    Only admins can list all users.
    """
    service = UserService(db)
    return service.get_all()

@router.get("/email/{email}", response_model=UserOutput)
async def get_user_by_email(
    email: str, db: DB_Dependancy, current_user: User = Depends(get_current_admin_user)
):
    """
    Only admins can get user details by email.
    """
    service = UserService(db)
    return service.get_by_email(email)

@router.get("/username/{username}", response_model=UserOutput)
async def get_user_by_username(
    username: str, db: DB_Dependancy, current_user: User = Depends(get_current_admin_user)
):
    """
    Only admins can get user details by username.
    """
    service = UserService(db)
    return service.get_by_username(username)

@router.get("/{user_id}", response_model=UserOutput)
async def get_user_by_id(
    user_id: UUID, db: DB_Dependancy, current_user: User = Depends(get_current_user)
):
    """
    Admins can get any user by ID.
    Normal users can only get their own user info.
    """
    service = UserService(db)
    user = service.get_by_id(user_id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if current_user.is_admin or current_user.id == user_id:
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to access this user"
        )

@router.patch("/{user_id}", response_model=UserOutput)
async def update_user(
    user_id: UUID, user: UserInput, db: DB_Dependancy, current_user: User = Depends(get_current_user)
):
    """
    Admins can update any user.
    Normal users can only update their own profile.
    """
    if not (current_user.is_admin or current_user.id == user_id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to update this user")

    service = UserService(db)
    return service.update_user(user_id, user)

@router.delete("/{user_id}", response_model=UserOutput)
async def delete_user(
    user_id: UUID, db: DB_Dependancy, current_user: User = Depends(get_current_admin_user)
):
    """
    Only admins can delete users.
    """
    service = UserService(db)
    return service.delete_user(user_id)