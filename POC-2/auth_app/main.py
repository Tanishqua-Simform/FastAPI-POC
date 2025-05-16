from fastapi import FastAPI
from utils.init_db import create_table
from router.users import user_router
from router.admin import admin_router

create_table()

app = FastAPI(
    title="POC-2: Auth-based User Profile API",
    summary="Build a simple API for user registration, authentication, and profile management. This POC will focus on authentication, authorization, and secure data handling.",
    description="### 1. User Registration and Login\n"
    "* Created Registration and Login API for Users. \n"
    "* Implemented Simple as well as JWT Authentication. \n"
    "* Used OAuth2Bearer request form for authenticating users over all secured endpoints.  \n"

    "### 2. User Profile Management \n"
    "* User can change their First and Last name and their Bio.  \n"
    "* Fields such as Email, Username and Gender can not be changed once registered.  \n"

    "### 3. Role-Based Access Control \n"
    "* Only admins can access the list of all users with their details. \n"
    "* Admins can change any user's role and their Account status (deleted or active.) \n"

    "### 4. Password Hashing and Security \n"
    "* Passwords are hashed using Passlib library for security reasons. \n"
    "* On login, entered password is verified with the hashed password. \n"

    "### 5. Database Integration \n"
    "* Connected PostgreSQL as Database. \n"
    "* With the help of event listeners, Parental Guidance for children is set on the basis of their age at the time of insertion in table. \n"
    "* User model validates the Email Id using Regular Expressions. (The validation can be performed in Pydantic schema as well but I chose to do it in model) \n"
)

app.include_router(user_router)
app.include_router(admin_router)