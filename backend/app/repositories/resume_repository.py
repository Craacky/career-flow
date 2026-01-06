from sqlalchemy.orm import Session

from app.models import Resume
from app.repositories.base_repository import BaseRepository


class ResumeRepository(BaseRepository[Resume]):
    def __init__(self, db: Session):
        super().__init__(Resume, db)

    def get_by_user(self, user_id: int) -> list[Resume]:
        return (self.db.query(Resume)
                .filter(Resume.user_id == user_id)
                .order_by(Resume.created_at.desc())
                .all())

    def get_latest_by_user(self, user_id: int) -> Resume | None:
        return (self.db.query(Resume)
                .filter(Resume.user_id == user_id)
                .order_by(Resume.created_at.desc())
                .first()
                )

    def count_by_user(self, user_id: int) -> int:
        return (self.db.query(Resume)
                .filter(Resume.user_id == user_id)
                .count()
                )

    def delete_by_user(self, user_id: int) -> int:
        count = self.db.query(Resume).filter(Resume.user_id == user_id).delete()
        self.db.commit()
        return count


