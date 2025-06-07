from fastapi import FastAPI

from calculator_logic import  Calculator

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Calculator API"}

@app.get("/calculate")
def handle_calculation(num1: float, num2: float, operation:str):
    calc = Calculator()
    result = calc.perform_calculation(num1, num2, operation)
    if isinstance(result, str):
        return {"status": "error", "result": result}
    else:
        return {"status": "success", "result": result}


