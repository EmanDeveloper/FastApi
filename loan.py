from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class LoanApplication(BaseModel):
    age:int
    income:float

@app.post("/loan-application")
def loan_application(application:LoanApplication):

    if(application.income>200000):
        return {"income ": application.income,}
    else:
        return "not approved"
