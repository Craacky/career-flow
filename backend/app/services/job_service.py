from sqlalchemy.orm import Session

from app.repositories.job_repository import JobRepository


class JobService:
    def __init__(self, db: Session):
        self.db = db
        self.job_repo = JobRepository(db)

    def get_job(self, job_id: int):
        return self.job_repo.get(job_id)

    def search_jobs(self, query: str, skip: int = 0, limit: int = 100):
        return self.job_repo.search(query, skip=skip, limit=limit)

    def filter_job(self,
                   experience_levels: list[str] | None = None,
                   work_formats: list[str] | None = None,
                   salary_min: float | None = None,
                   salary_max: float | None = None,
                   skip: int = 0,
                   limit: int = 20):
        jobs = self.job_repo.get_all(skip=skip, limit=limit * 10)
        if experience_levels:
            jobs = [j for j in jobs if j.experience_level in experience_levels]
        if work_formats:
            jobs = [j for j in jobs if j.work_format in work_formats]
        if salary_min:
            jobs = [j for j in jobs if j.salary_max >= salary_min]
        if salary_max:
            jobs = [j for j in jobs if j.salary_min <= salary_max]

        return jobs[:limit]

    def get_fresh_jobs(self, days: int = 7, limit: int = 20):
        return self.job_repo.get_recent_jobs(days=days, limit=limit)
