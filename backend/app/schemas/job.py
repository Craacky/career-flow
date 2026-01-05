from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List


class JobCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=255)
    company: str = Field(..., min_length=1, max_length=255)
    location: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    requirements: Optional[str] = None
    tech_stack: Optional[str] = None
    salary_min: Optional[float] = Field(None, ge=0)
    salary_max: Optional[float] = Field(None, ge=0)
    currency: str = Field(default="USD", max_length=10)
    url: str = Field(..., max_length=500)
    source: str = Field(..., max_length=50)
    experience_level: Optional[str] = None
    employment_type: Optional[str] = None
    work_format: Optional[str] = None
    published_at: Optional[datetime] = None


class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    location: Optional[str]
    salary_min: Optional[float]
    salary_max: Optional[float]
    currency: str
    source: str
    experience_level: Optional[str]
    work_format: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class JobDetailResponse(JobResponse):
    description: Optional[str]
    requirements: Optional[str]
    tech_stack: Optional[str]
    employment_type: Optional[str]
    published_at: Optional[datetime]
    updated_at: datetime


class JobFilter(BaseModel):
    experience_level: Optional[List[str]] = None
    work_format: Optional[List[str]] = None
    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
    tech_stack: Optional[List[str]] = None
    search_query: Optional[str] = None
