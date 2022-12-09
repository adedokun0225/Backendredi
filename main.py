from fastapi import FastAPI 
from dotenv import dotenv_values
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware




#from routes import router as quiz_router


config = dotenv_values(".env")

#APP object
app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
    
)

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient("mongodb+srv://Adekunle:adorneng02@quizredi.kfhsp8z.mongodb.net/?retryWrites=true&w=majority")
    app.database = app.mongodb_client.quizredi
    collection = app.database.quizredi
    return collection
 

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
    
    
#app.include_router(Quiz_router, tags=["Quiz"], prefix="/Quiz")







