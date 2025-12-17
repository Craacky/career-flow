from fastapi import FastAPI
from app import __version__
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.middleware.error_handler import setup_error_handlers
from app.api.router import api_router

app = FastAPI(
    title="CareerFlow API",
    description="LinkedIn Job Scout + AI Resume Optimizer",
    version= __version__,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

setup_error_handlers(app)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "ok"}
