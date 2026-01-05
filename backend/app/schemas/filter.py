from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class FilterCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    criteria: dict = Field(...)


class FilterUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    criteria: Optional[dict] = None


class FilterResponse(BaseModel):
    id: int
    user_id: int
    name: str
    criteria: dict
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class FilterListResponse(BaseModel):
    id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True
