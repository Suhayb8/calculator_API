# Calculator API

A simple calculator API built with FastAPI that performs basic arithmetic operations: add, subtract, multiply, and divide.

## How to Run

1. Make sure you have Python 3.7+ installed  
2. Install dependencies (if any)
   ```bash
   pip install fastapi uvicorn
   ```
3. Run the API server:
   ```bash
   uvicorn main:app --reload
   ```
4. Open your browser or API tool (Postman) and visit:
   ```
   http://127.0.0.1:8000/
   ```
5. Test calculation endpoint, for example:
   ```
   http://127.0.0.1:8000/calculate?num1=10&num2=5&operation=add
   ```

## Endpoints

* `/` - Welcome message  
* `/calculate` - Perform calculation with parameters:  
  * `num1` (float)  
  * `num2` (float)  
  * `operation` (string: add, subtract, multiply, divide)  

## Example Response

Successful response:

```json
{
  "status": "success",
  "result": 15
}
```

Error response (e.g., divide by zero):

```json
{
  "status": "error",
  "message": "Cannot divide by zero!"
}
```
