from sqlalchemy.orm import Session
from app.models.filter import UserFilter
from app.repositories.base_repository import BaseRepository


class FilterRepository(BaseRepository[UserFilter]):
    def __init__(self, db: Session):
        super().__init__(UserFilter, db)

    def get_by_user(self, user_id: int) -> list[UserFilter]:
        return (self.db.query(UserFilter)
                .filter(UserFilter.user_id == user_id)
                .order_by(UserFilter.created_at.desc())
                .all())

    def get_by_user_and_id(self, user_id: int, filter_id: int) -> UserFilter | None:
        return (self.db.query(UserFilter)
                .filter(UserFilter.user_id == user_id, UserFilter.id == filter_id)
                .first())

    def count_by_user(self, user_id: int) -> int:
        return (self.db.query(UserFilter)
                .filter(UserFilter.user_id == user_id)
                .count())

    def delete_by_user(self, user_id: int) -> int:
        count = self.db.query(UserFilter).filter(UserFilter.user_id == user_id).delete()
        self.db.commit()
        return count

    def delete_by_user_and_id(self, user_id: int, filter_id: int) -> bool:
        f = self.get_by_user_and_id(user_id, filter_id)
        if f:
            self.db.delete(f)
            self.db.commit()
            return True
        return False
    