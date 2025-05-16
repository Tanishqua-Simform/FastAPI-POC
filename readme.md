# FastAPI Proof of Concepts

I have implemented 2 POCs in FastAPI, both featuring some important concepts such as Auth, CRUD and so on.

## Project Structure

```
FastAPI-POC/
├── POC-1/                       # To-Do List API
│   ├── todo_app/
│   │   ├── config/              # SQLite config
│   │   ├── models/              # SQLAlchemy models
│   │   ├── repository/          # CRUD operations
│   │   ├── router/              # API endpoints
│   │   ├── schemas/             # Pydantic schemas
│   │   ├── services/            # Business logic
│   │   ├── utils/               # Utility functions
|   │   ├── main.py              # FastAPI app launcher
|   │   └── __init__.py
|   |
│   └── requirements.txt         # Dependencies for Poc-1
|
├── POC-2/                       # Auth-Based User Profile API
│   ├── auth_app/
│   │   ├── config/              # PostgreSQL config
│   │   ├── models/              # SQLAlchemy models
│   │   ├── repository/          # User and admin operations
│   │   ├── routes/              # Register and Profile endpoints
│   │   ├── schemas/             # Request/response validation
│   │   ├── services/            # Auth & RBAC logic
│   │   └── utils/               # Password hashing, JWT, etc.
|   │   ├── main.py              # FastAPI app launcher
|   │   └── __init__.py
|   |
│   └── requirements.txt         # Dependencies for Poc-2
|
└── README.md                    # You're here!
```

## POC 1: To-Do List API

A simple and clean REST API for managing to-do tasks.

### Highlights

- **CRUD Operations**: Add, update, list, and delete tasks.
- **Pydantic Validation**:

  - Title must be unique
  - Due date must be in the future
  - Status must be `"Pending"` or `"Completed"`

- **Dependency Injection**: Used `Depends()` for database session handling.
- **Database**: Lightweight integration using **SQLite**.
- **Error Handling**: Graceful response for invalid operations and missing records.
- **Swagger Enhancements**:

  - Placeholder values and metadata for better UX
  - Function docstrings, tags, and summaries added

### Output

- Accessible via: `http://localhost:8000/docs`

![ToDo Swagger Screenshot](/images/POC-1.1.png)
![ToDo Swagger Screenshot](/images/POC-1.2.png)
![ToDo Swagger Screenshot](/images/POC-1.3.png)

## POC 2: Auth-Based User Profile API

A secure API for user management with JWT authentication and role-based access control.

### 🎯 Highlights

- **JWT Authentication**:

  - Simple and secure login flow using OAuth2 with password bearer
  - Protected endpoints with token-based access

- **User Registration & Profile Management**:

  - Editable: First name, last name, bio
  - Immutable: Email, username, gender

- **Admin Privileges**:

  - View all users
  - Modify any user's role and account status

- **Password Security**:

  - Hashed using `Passlib`
  - Secure login with hash comparison

- **Database Integration**:

  - Used **PostgreSQL** via SQLAlchemy
  - Age-based logic (e.g., parental guidance) with lifecycle events
  - Regex validation on email format directly in the model

### Output

- Accessible via: `http://localhost:9000/docs`

![Auth Swagger Screenshot](/images/POC-2.1.png)
![Auth Swagger Screenshot](/images/POC-2.2.png)
![Auth Swagger Screenshot](/images/POC-2.3.png)

## Setup Instructions

1. **Clone this repository**

```bash
git clone https://github.com/Tanishqua-Simform/FastAPI-POC.git
cd FastAPI-POC
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run each POC**

```bash
# POC 1 - ToDo App
cd POC-1/todo_app
uvicorn main:app --reload

# POC 2 - Auth App
cd ../POC-2/auth_app
uvicorn main:app --reload
```

###### Thank you for stopping by!
