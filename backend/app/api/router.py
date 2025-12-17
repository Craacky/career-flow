from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/health")
async def api_health():
    return {"message": "API is healthy"}