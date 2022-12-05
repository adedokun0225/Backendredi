from fastapi import APIRouter
from models.user import user
from config.db import Connection

user = APIRouter()

@user.get('/')
async def get_Questions():
    return Connection.local.user.find()

