from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from schemas.todo_schema import TodoInput, TodoOutput

from service.todo_service import TodoService
from config.database import get_db
from dependancy.auth import get_current_user
from models.user_model import User

router = APIRouter(prefix="/todos", tags=["Todos"])

@router.post("/", response_model=TodoOutput)
def create_todo(todo_in: TodoInput, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Create a new todo item.
    """
    service = TodoService(db)
    return service.create_todo(todo_in, current_user)

@router.get("/", response_model=List[TodoOutput])
def get_all_todos(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Get all todo items.
    """
    service = TodoService(db)
    return service.get_all_todos(current_user)

@router.get("/{todo_id}", response_model=TodoOutput)
def get_todo(todo_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Get a todo item by ID.
    """
    service = TodoService(db)
    todo = service.get_todo_by_id(todo_id, current_user)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/{todo_id}", response_model=TodoOutput)
def update_todo(todo_id: int, todo_in: TodoInput, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Update a todo item by ID.
    """
    service = TodoService(db)
    updated_todo = service.update_todo(todo_id, todo_in, current_user)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Delete a todo item by ID.
    """
    service = TodoService(db)
    deleted_todo = service.delete_todo(todo_id, current_user)
    if not deleted_todo:
        raise HTTPException(status_code=404, detail="Todo not found")