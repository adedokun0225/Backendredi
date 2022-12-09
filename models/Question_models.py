from pydantic import BaseModel, Field
import uuid
from typing import Optional

class Quiz(BaseModel):
    quiz: str
    question:str
    answer: str
    evaluation: int
   



class Response(BaseModel):
    quiz: Optional [str]
    question: Optional[str]
    answer: Optional[str]
    
    
    
# class Question_Update(BaseModel):
#     quiz: Optional[str]
#     question: Optional[str]
#     answer: Optional[str]
    
    
    
    