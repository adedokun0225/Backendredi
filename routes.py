from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from models.Question_models import Quiz, Response

from handler import (fetch_one_Question,
                   fetch_all_Questions,
                   create_Questions,
                   update_question,
                   remove_Question
                   )


router = APIRouter()


@router.get("/api/Quiz")
def read_root():
    return {"i love football"}


@router.get("/api/Quiz{quiz}", response_model= Response)
async def get_Quiz():
    response = await fetch_all_Questions()
    return response

@router.get("/api/Quiz{id}")
async def get_Question_by_quiz(quiz):
    response = await fetch_one_Question(quiz)
    if response is True:
        return response
    raise HTTPException(404, f"there is no Question with this quiz {quiz}")

@router.post("/api/Quiz", response_model = Response)
async def post_Question(quiz:Quiz):
    response = await create_Questions(quiz.dict())
    if response:
        return response
    raise HTTPException(400, "Bad request")

@router.put("/api/Quiz{quiz}/",response_model= Response)
async def put_Question(quiz:str, question:str):
    response = await update_question(quiz, question)
    if response:
        return response
    raise HTTPException (400, f"there is no question with this quiz {quiz}")

@router.delete("/api/Quiz{quiz}")
async def delete_Question(quiz):
    response = await remove_Question(quiz)
    if response:
        return "Successfully deleted the quiz"
    raise HTTPException (f"there is no question with this quiz {quiz}")
