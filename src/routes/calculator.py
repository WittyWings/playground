from fastapi import APIRouter, HTTPException, Request, Response
from pydantic import BaseModel, validator
from typing import Any

from src.services.calculator import evaluate_expression, CalculatorError

router = APIRouter()

class CalcRequest(BaseModel):
    expression: str

    @validator('expression')
    def check_expression(cls, v: str) -> str:
        # Simple validation: ensure only allowed characters
        allowed = set('0123456789+-*/%(). ')  # spaces allowed for readability
        if not set(v) <= allowed:
            raise ValueError('Expression contains invalid characters')
        return v

@router.post('/api/calculator')
async def calculate(request: Request, payload: CalcRequest, response: Response) -> Any:
    try:
        result = evaluate_expression(payload.expression)
        # Add rate limit header (example static value)
        response.headers['X-RateLimit-Limit'] = '100'
        response.headers['X-RateLimit-Remaining'] = '99'
        return {'result': result}
    except CalculatorError as e:
        raise HTTPException(status_code=400, detail=str(e))
