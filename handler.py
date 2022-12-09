from fastapi import APIRouter, Body, Request, HTTPException, status
from models.Question_models import Quiz, Response
from main import startup_db_client, shutdown_db_client


async def fetch_one_Question(quiz):
    Question = await startup_db_client.find_one({"Quiz": quiz})
    return Question

async def fetch_all_Questions():
    Questions = []
    cursor = startup_db_client.find({})
    async for Question in cursor:
        Questions.append(Quiz(**Question))
    return Questions

async def create_Questions(Question):
    document = Question
    result = await startup_db_client.insert_one(document)
    return result


async def update_Question(quiz, question):
    await startup_db_client.update_one({"Quiz":quiz}, {"$set":{
        "Questions":question}})
    document = await startup_db_client.find_one({"Quiz": quiz})
    return document

async def remove_Question(quiz):
    await startup_db_client.delete_one({"Quiz":quiz})
    return True