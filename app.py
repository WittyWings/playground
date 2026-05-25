from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Literal

from calculator_service import add, subtract, multiply, divide, CalculatorError

app = FastAPI()

class CalcRequest(BaseModel):
    op: Literal["add", "subtract", "multiply", "divide"]
    a: float
    b: float

class CalcResponse(BaseModel):
    result: float

@app.post("/api/calculator", response_model=CalcResponse)
async def calculate(req: CalcRequest):
    try:
        if req.op == "add":
            result = add(req.a, req.b)
        elif req.op == "subtract":
            result = subtract(req.a, req.b)
        elif req.op == "multiply":
            result = multiply(req.a, req.b)
        elif req.op == "divide":
            result = divide(req.a, req.b)
        else:
            raise CalculatorError("INVALID_OPERATION", "Unsupported operation")
        return {"result": result}
    except CalculatorError as exc:
        raise HTTPException(status_code=400, detail={"error": exc.code})
