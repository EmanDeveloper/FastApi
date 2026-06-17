from fastapi import FastAPI

app=FastAPI()

@app.get("/") #decorator to define the route for the root endpoint
def read_root():
    return {"First Fast Api route": "Hello World"}