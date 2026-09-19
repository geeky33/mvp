from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.questions import router as questions_router


app = FastAPI(
    title="AI Confidence Calibration",
    description="A system for estimating and evaluating AI reasoning confidence.",
    version="0.1.0",
)


app.include_router(
    health_router,
    prefix="/api"
)

app.include_router(
    questions_router,
    prefix="/api"
)


@app.get("/")
def root():
    return {
        "name": "AI Confidence Calibration",
        "status": "running",
        "version": "0.1.0",
    }