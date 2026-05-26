from fastapi import FastAPI

# Import existing routers if any; placeholder for other imports

app = FastAPI(title='Calculator API')

# Include the calculator router
from src.routes.calculator import router as calculator_router
app.include_router(calculator_router)

# If there are other routers, they would be included here as well.
