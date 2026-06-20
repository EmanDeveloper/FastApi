from fastapi import FastAPI

app=FastAPI()

@app.get("/") #decorator to define the route for the root endpoint
def read_root():
    return {"First Fast Api route": "Hello World"}

@app.get("/customer/{cutomer_id}")#path parameter
def read_customer(customer_id: int):
    return {"customer_id": customer_id, "name": "John Doe", "email": "john.doe@example.com"}

@app.get("/cutomer")
def get_customer_detail(age:int,gender:str):
    return {"age":age,"gender":gender}
