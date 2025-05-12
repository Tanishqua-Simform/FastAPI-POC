from fastapi import FastAPI
from utils.init_db import create_table
from router.users import user_router
from router.posts import post_router 
from router.admin import admin_router

create_table()

app = FastAPI()

app.include_router(user_router)
app.include_router(post_router)
app.include_router(admin_router)