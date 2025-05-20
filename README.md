# FastAPI Todo App

A FastAPI-based Todo application with user authentication, JWT-based authorization, and PostgreSQL database support. The project uses SQLAlchemy ORM, Alembic for migrations, and Pydantic for data validation.

## Features

- User registration and authentication (JWT)
- Admin and regular user roles
- CRUD operations for Todo items
- PostgreSQL database with SQLAlchemy ORM
- Alembic migrations
- Password hashing with bcrypt

## Project Structure

```
.
├── alembic/                # Alembic migration scripts
├── config/                 # Database configuration
├── dependancy/             # Authentication dependencies
├── models/                 # SQLAlchemy models
├── repository/             # Data access layer
├── routers/                # FastAPI routers
├── schemas/                # Pydantic schemas
├── service/                # Business logic
├── utils/                  # Utility functions (auth, security, etc.)
├── main.py                 # FastAPI application entrypoint
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
```

## Setup

1. **Clone the repository**

   ```sh
   git clone <repo-url>
   cd POC\ Exercises
   ```

2. **Create and activate a virtual environment**

   ```sh
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Edit `.env` as needed.

5. **Run Alembic migrations**

   ```sh
   alembic upgrade head
   ```

6. **Start the FastAPI server**

   ```sh
   uvicorn main:app --reload
   ```

## API Endpoints

- `/auth/login` - User login
- `/auth/refresh` - Refresh JWT token
- `/users` - User registration and management
- `/todos` - Todo CRUD operations

## License

MIT License