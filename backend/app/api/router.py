from fastapi import APIRouter

api_router = APIRouter()

from app.api.v1 import auth, users, jobs

api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(jobs.router)

@api_router.get("/health")
def health_check():
    return {"status": "ok"}

