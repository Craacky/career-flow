from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.db.session import get_db
from app.schemas.job import JobResponse, JobDetailResponse
from app.schemas.common import PaginatedResponse
from app.services import JobService

router = APIRouter(
    prefix="/jobs",
    tags=["jobs"],
)


@router.get("/", response_model=PaginatedResponse[JobResponse])
def get_jobs(
        skip: int = 0,
        limit: int = 20,
        experience_levels: List[str] = None,
        work_format: List[str] = None,
        salary_min: float = None,
        salary_max: float = None,
        db: Session = Depends(get_db)
):
    service = JobService(db)
    jobs = service.filter_job(
        experience_levels=experience_levels,
        work_formats=work_format,
        salary_min=salary_min,
        salary_max=salary_max,
        skip=skip,
        limit=limit
    )
    total = service.job_repo.count()
    page = (skip // limit) + 1 if limit > 0 else 1

    return {
        "total": total,
        "page": page,
        "page_size": limit,
        "items": jobs,
    }


@router.get("/search", response_model=List[JobResponse])
def search_jobs(
        q: str,
        limit: int = 20,
        db: Session = Depends(get_db)
):
    if not q or len(q) < 2:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Search query must be at least 2 characters")
    service = JobService(db)
    jobs = service.search_jobs(query=q, limit=limit)
    return jobs


@router.get("/{job_id}", response_model=JobDetailResponse)
def get_job_details(job_id: int, db: Session = Depends(get_db)):
    service = JobService(db)
    job = service.get_job(job_id)

    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
