from fastapi import FastAPI

from calculator import  add, subtract, multiply, divide

app = FastAPI()

@app.get("/Welcome")
def home_cal():
    return {"message": "🧮Welcome to Calculator API"}

@app.get("/add/{x}/{y}")
def add_route(x: float, y: float):
    return {"result": add(x , y)}

@app.get("/subtract/{x}/{y}")
def subtract_route(x: float, y: float):
    return {"result": subtract(x,y)}

@app.get("/multiply/{x}/{y}")
def multiply_route(x: float, y: float):
    return {"result": multiply(x,y)}

@app.get("/divide/{x}/{y}")
def divide_route(x: float, y: float):
    return {"result": divide(x, y)}




