def userEntity(Questions) -> dict:
    return {
        "id":str(Questions["_id"]),
        "Question": Questions["name"],
        "Options": Questions["Options"],
        "Answer": Questions["Answer"]  
    }
    
