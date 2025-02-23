# FastAPI Demo Application

A modern and scalable backend API built with FastAPI framework.
Built on python 3.9


## Project Structure

The project is organized into the following key directories:

- `app/`: Contains the main application code.
- `app/api/`: Defines the API endpoints.
- `app/core/`: Contains core functionality like database and configuration.
- `app/schemas/`: Defines Pydantic models for request/response validation.
- `app/crud/`: Contains CRUD operations for database models.


## Setup

1. Install dependencies using pip:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
uvicorn app.main:app --reload
```

3. Access the API documentation at:

```bash
http://localhost:8000/docs
```


## API Endpoints

The API provides the following endpoints:

### User Management

- `POST /users/`: Create a new user.
- `GET /users/{user_id}/`: Get a user by ID.







