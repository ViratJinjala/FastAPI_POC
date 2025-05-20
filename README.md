# FastAPI POC

This project is a FastAPI-based Proof of Concept (POC) for user authentication, todo management, and user administration. It demonstrates the use of FastAPI, SQLAlchemy, Alembic, JWT authentication, and PostgreSQL.

---

## 🚀 Features

- **User registration and authentication** (JWT-based)
- **Admin and regular user roles** with role-based access control
- **CRUD operations for todo items** (per user)
- **User profile management**
- **Secure password hashing** with bcrypt
- **Alembic migrations** for database schema
- **Modular project structure** for scalability and maintainability

---

## 🗂️ Project Structure

```
.
├── main.py                 # FastAPI app entry point
├── router/                 # API route definitions (auth, user, todo)
├── models/                 # SQLAlchemy ORM models
├── schemas/                # Pydantic schemas for request/response
├── repository/             # Database access logic
├── service/                # Business logic
├── utils/                  # Utility functions (auth, security, db init)
├── config/                 # Database configuration
├── dependancy/             # Dependency injection for authentication
├── alembic/                # Database migrations
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
```

---

## ⚙️ Setup

1. **Clone the repository**
2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure your database**
   - Update the database URL in `config/database.py` or your `.env` file.
5. **Run Alembic migrations**
   ```bash
   alembic upgrade head
   ```
6. **Start the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```

---

## 🔑 API Endpoints

### Auth Endpoints (`/auth`)
| Method | Path      | Description                    |
|--------|-----------|--------------------------------|
| POST   | /login    | User login, returns JWT tokens |
| POST   | /refresh  | Refresh access token           |

### User Endpoints (`/users`)
| Method | Path                  | Description                                 |
|--------|-----------------------|---------------------------------------------|
| POST   | /                     | Register a new user                         |
| GET    | /profile              | Get current user's profile                  |
| PATCH  | /profile              | Update current user's profile               |
| GET    | /                     | List all users (admin only)                 |
| GET    | /email/{email}        | Get user by email (admin only)              |
| GET    | /username/{username}  | Get user by username (admin only)           |
| GET    | /{user_id}            | Get user by ID (admin or self)              |
| PATCH  | /{user_id}            | Update user by ID (admin or self)           |
| DELETE | /{user_id}            | Delete user by ID (admin only)              |

### Todo Endpoints (`/todos`)
| Method | Path        | Description                        |
|--------|-------------|------------------------------------|
| POST   | /           | Create a new todo                  |
| GET    | /           | List all todos for current user    |
| GET    | /{todo_id}  | Get a specific todo by ID          |
| PUT    | /{todo_id}  | Update a todo by ID                |
| DELETE | /{todo_id}  | Delete a todo by ID                |

---

## 🌐 Live Server

[Open API Docs](https://fastapi-poc-1-krpl.onrender.com)

---
