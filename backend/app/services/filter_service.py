import json

from sqlalchemy.orm import Session

from app.repositories.filter_repository import FilterRepository


class FilterService:
    def __init__(self, db: Session):
        self.MAX_FILTER_PER_USER = 10
        self.db = db
        self.filter_repo = FilterRepository(db)

    def create_filter(self, user_id: int, name: str, criteria: dict):
        self._validate_filter_name(name)
        self._validate_criteria(criteria)

        count = self.filter_repo.count_by_user(user_id)
        if count >= self.MAX_FILTER_PER_USER:
            raise ValueError(f"Filter have reached maximum limit {self.MAX_FILTER_PER_USER}")

        criteria_json = json.dumps(criteria)
        return self.filter_repo.create({
            "user_id": user_id,
            "name": name,
            "criteria": criteria_json
        })

    def get_user_filters(self, user_id: int):
        return self.filter_repo.get_by_user(user_id)

    def get_filter(self, user_id: int, filter_id: int):
        return self.filter_repo.get_by_user_and_id(user_id, filter_id)

    def update_filter(self, user_id: int, filter_id: int, name: str, criteria: dict = None):
        f = self.filter_repo.get_by_user_and_id(user_id, filter_id)
        if not f:
            return None
        updated_data = {}

        if name is not None:
            self._validate_filter_name(name)
            updated_data["name"] = name
        if criteria is not None:
            self._validate_criteria(criteria)
            updated_data["criteria"] = json.dumps(criteria)
        if updated_data:
            return self.filter_repo.update(filter_id, updated_data)
        return f

    def delete_filter(self, user_id: int, filter_id: int) -> bool:
        return self.filter_repo.delete_by_user_and_id(user_id, filter_id)

    @staticmethod
    def _validate_filter_name(name: str) -> None:
        if not name:
            raise ValueError("Filter name is required")
        if len(name) < 3:
            raise ValueError("Filter name must be at least 3 characters long")
        if len(name) > 255:
            raise ValueError("Filter name is too long")

    @staticmethod
    def _validate_criteria(criteria: dict) -> None:
        if not isinstance(criteria, dict):
            raise ValueError("Criteria must be a dictionary")
        if not criteria:
            raise ValueError("Criteria cannot be empty")

        allowed_keys = {
            "experience_level",
            "tech_stack",
            "work_format",
            "salary_min",
            "salary_max",
            "source"
        }
        for key in criteria.keys():
            if key not in allowed_keys:
                raise ValueError(f"Criteria key {key} is invalid")
