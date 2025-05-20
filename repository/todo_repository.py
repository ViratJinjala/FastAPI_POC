from sqlalchemy.orm import Session
from models.todo_model import ToDo
from schemas.todo_schema import TodoInput,TodoOutput
from models.user_model import User

class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, todo_in: TodoInput, current_user: User):
        todo = ToDo(
            title=todo_in.title,
            description=todo_in.description,
            status=todo_in.status,
            due_date=todo_in.due_date,
            user_id=current_user.id
        )
        self.db.add(todo)
        self.db.commit()
        self.db.refresh(todo)
        return todo

    def get_all_by_user(self, user: User):
        return self.db.query(ToDo).filter(ToDo.user_id == user.id).all()

    def get_by_id(self, todo_id: int, user: User):
        return self.db.query(ToDo).filter(ToDo.id == todo_id, ToDo.user_id == user.id).first()

    def update(self, todo_id: int, todo_in: TodoInput, user: User):
        todo = self.get_by_id(todo_id, user)
        if not todo:
            return None
        for key, value in todo_in.model_dump(exclude_unset=True).items():
            setattr(todo, key, value)
        self.db.commit()
        self.db.refresh(todo)
        return todo

    def delete(self, todo_id: int, user: User):
        todo = self.get_by_id(todo_id, user)
        if not todo:
            return None
        self.db.delete(todo)
        self.db.commit()
        return todo