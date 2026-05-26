from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

# Import existing routers if any; placeholder for other imports

app = FastAPI(title='Calculator API')

# Include the calculator router
from src.routes.calculator import router as calculator_router
app.include_router(calculator_router)

# Global exception handler for request validation errors to return 400
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Return a JSON response with a 400 status and a generic error message
    return JSONResponse(status_code=400, content={"error": "Invalid expression"})

# If there are other routers, they would be included here as well.
