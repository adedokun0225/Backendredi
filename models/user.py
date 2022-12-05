from pydantic import BaseModel

class Questions(BaseModel):
    Question: str
    Option: str
    Answer: str
    
    