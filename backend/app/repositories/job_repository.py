from sqlalchemy.orm import Session
from sqlalchemy import or_
from datetime import datetime, timedelta

from app.models import Job
from app.repositories.base_repository import BaseRepository


class JobRepository(BaseRepository[Job]):
    def __init__(self, db: Session):
        super().__init__(Job, db)

    def get_by_url(self, url: str) -> Job | None:
        return self.db.query(Job).filter(Job.url == url).first()

    def search(self, query: str, skip: int = 0, limit: int = 20) -> list[Job]:
        return (self.db.query(Job).filter(
            or_(Job.title.ilike(f"%{query}%"), Job.company.ilike(f"%{query}%")))
                .offset(skip)
                .limit(limit)
                .all()
                )

    def filter_by_experience(self, experience_level: list[str], skip: int = 0, limit: int = 20) -> list[Job]:
        return (self.db.query(Job)
                .filter(Job.experience_level.in_(experience_level))
                .offset(skip)
                .limit(limit)
                .all())

    def filter_by_work_format(self, work_formats: list[str], skip: int = 0, limit: int = 20) -> list[Job]:
        return (self.db.query(Job)
                .filter(Job.work_format.in_(work_formats))
                .offset(skip)
                .limit(limit)
                .all())

    def filter_by_salary_range(self, min_salary: float | None = None, max_salary: float | None = None, skip: int = 0,
                               limit: int = 20) -> list[Job]:
        query = self.db.query(Job)

        if min_salary is not None:
            query = query.filter(Job.salary_max >= min_salary)

        if max_salary is not None:
            query = query.filter(Job.salary_min <= max_salary)

        return query.offset(skip).limit(limit).all()

    def get_recent_jobs(self, days: int = 7, limit: int = 20) -> list[Job]:
        since = datetime.now() - timedelta(days=days)
        return (self.db.query(Job)
                .filter(Job.created_at >= since)
                .order_by(Job.created_at.desc())
                .limit(limit)
                .all())

    def get_by_source(self, source: str, limit: int = 20) -> list[Job]:
        return (self.db.query(Job)
                .filter(Job.source == source)
                .limit(limit)
                .all())
