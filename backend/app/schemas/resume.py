from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field


class ResumeCreate(BaseModel):
    notes: Optional[str] = Field(None, max_length=255)


class ResumeAnalysis(BaseModel):
    strengths: Optional[List[str]] = None
    improvements: Optional[List[str]] = None
    recommendations: Optional[List[str]] = None
    scores: Optional[int] = Field(None, ge=0, le=100)


class ResumeResponse(BaseModel):
    id: int
    filename: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
