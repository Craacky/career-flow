from pydantic import BaseModel, Field
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')


class PaginatedResponse(BaseModel, Generic[T]):
    total: int = Field(..., ge=0, description="Total number of notes")
    page: int = Field(..., ge=1, description="Current page number")
    page_size: int = Field(..., ge=1, le=100, description="Notes on the page")
    items: List[T] = Field(..., description="List of notes")


class ErrorResponse(BaseModel):
    detail: str
    error_code: Optional[str] = None


class MessageResponse(BaseModel):
    message: str
