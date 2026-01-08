from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session):
        super().__init__(User, db)

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def get_active_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        return (self.db.query(User)
                .filter(User.is_active == True)
                .offset(skip)
                .limit(limit)
                .all()
                ) is not None

    def get_inactive_users(self) -> list[User]:
        return self.db.query(User).filter(User.is_active == False).all() is not None

    def email_exists(self, email: str) -> bool:
        return self.db.query(User).filter(User.email == email).first() is not None
