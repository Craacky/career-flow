from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.repositories.subscription_repository import SubscriptionRepository
from app.core.security import verify_password, hash_password


class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)
        self.subscription_repo = SubscriptionRepository(db)

    def create_user(self, email: str, password: str, full_name: str | None = None) -> User:
        self._validate_email(email)
        self._validate_password(password)

        if self.user_repo.email_exists(email):
            raise ValueError(f"Email {email} already registered")
        hashed_password = hash_password(password)

        user = self.user_repo.create({
            "email": email,
            "hashed_password": hashed_password,
            "full_name": full_name,
            "is_active": True,
        })

        self.subscription_repo.create({
            "user_id": user.id,
            "plan": "free",
            "is_active": True,
            "price": 0.0
        })

        return user

    def authenticate_user(self, email: str, password: str) -> User | None:
        user = self.user_repo.get_by_email(email)

        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        if not user.is_active:
            return None
        return user

    def get_user(self, user_id: int) -> User | None:
        return self.user_repo.get(user_id)

    def update_user(self, user_id: int, full_name: str | None = None, email: str | None = None) -> User | None:
        user = self.user_repo.get(user_id)
        if not user:
            return None

        updated_data = {}

        if full_name is not None:
            updated_data["full_name"] = full_name
        if email is not None:
            if email != user.email and self.user_repo.email_exists(email):
                raise ValueError(f"Email {email} already in use")
            updated_data["email"] = email
        if updated_data:
            return self.user_repo.update(user_id, updated_data)
        return user

    @staticmethod
    def _validate_email(email: str) -> None:
        if not email:
            raise ValueError("Email is required")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format")

        if len(email) > 255:
            raise ValueError("Email is too long")

    @staticmethod
    def _validate_password(password: str) -> None:
        if not password:
            raise ValueError("Password is required")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if len(password) > 255:
            raise ValueError("Password is too long")
