from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from config.database import get_db
from repository.user_repository import UserRepository
from utils.auth import create_access_token, create_refresh_token, verify_token
from utils.security import verify_password
from schemas.auth_schema import Token
from models.user_model import User

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    User login endpoint.
    """
    user_repo = UserRepository(db)
    user = user_repo.get_by_username(form_data.username)

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token({"username": user.username})
    refresh_token = create_refresh_token({"username": user.username})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.post("/refresh", response_model=Token)
def refresh_token(refresh_token: str = Query(...)):
    """
    Refresh access token using refresh token.
    """
    payload = verify_token(refresh_token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    username = payload.get("sub")
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    new_access_token = create_access_token({"username": username})
    new_refresh_token = create_refresh_token({"username": username})

    return {
        "access_token": new_access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer"
    }