from sqlalchemy.orm import Session
from app.repositories.job_repository import JobRepository
from app.repositories.subscription_repository import SubscriptionRepository
from app.repositories.filter_repository import FilterRepository
import json


class NotificationService:
    def __init__(self, db: Session):
        self.db = db
        self.job_repo = JobRepository(db)
        self.subscription_repo = SubscriptionRepository(db)
        self.filter_repo = FilterRepository(db)

    def notify_new_jobs(self, user_id: int, jobs: list) -> dict:
        if not jobs:
            return {
                "sent": False,
                "count": 0,
                "message": "No new jobs found"
            }
        return {
            "sent": True,
            "count": len(jobs),
            "message": f"Found {len(jobs)} new jobs"
        }

    def notify_subscriptions_expiring(self, user_id: int, ) -> dict:
        sub = self.subscription_repo.get_by_user(user_id)
        if not sub or not sub.is_active:
            return {"sent": False, "message": "No active subscription found"}
        return {
            "sent": True,
            "message": f"Subscription expiring on {sub.expires_at}"
        }

    def _filter_jobs_by_criteria(self, jobs: list, filters: list) -> list:
        matching = []

        for job in jobs:
            for f in filters:
                criteria = json.loads(f.criteria)
                if self._job_matches_criteria(job, criteria):
                    matching.append(job)
                    break

        return matching

    @staticmethod
    def _job_matches_criteria(job, criteria: dict) -> bool:
        if "experience_level" in criteria:
            levels = criteria["experience_level"]
            if job.experience_level not in levels:
                return False

        if "work_format" in criteria:
            formats = criteria["work_format"]
            if isinstance(formats, str):
                formats = [formats]
            if job.work_format not in formats:
                return False
        if "salary_min" in criteria and job.salary_max:
            if job.salary_max < criteria["salary_min"]:
                return False

        if "salary_max" in criteria and job.salary_min:
            if job.salary_min > criteria["salary_max"]:
                return False

        if "tech_stack" in criteria:
            job_techs = json.loads(job.tech_stack) if job.tech_stack else []
            criteria_techs = criteria["tech_stack"]
            if not any(tech in job_techs for tech in criteria_techs):
                return False

        return True
