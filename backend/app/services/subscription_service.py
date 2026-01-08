from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.repositories.subscription_repository import SubscriptionRepository


class SubscriptionService:
    def __init__(self, db: Session):
        self.db = db
        self.subscription_repository = SubscriptionRepository(db)

    def get_subscription(self, user_id: int):
        return self.subscription_repository.get_by_user(user_id)

    def is_pro(self, user_id: int) -> bool:
        return self.subscription_repository.is_pro(user_id)

    def is_active(self, user_id: int) -> bool:
        return self.subscription_repository.is_active(user_id)

    def upgraded_to_pro(self, user_id: int, days: int = 30):
        expires_at = datetime.now() + timedelta(days=days)
        return self.subscription_repository.update(user_id, {
            "plan": "pro",
            "is_active": True,
            "price": 5.99,
            "expires_at": expires_at
        })

    def downgraded_to_free(self, user_id: int):
        return self.subscription_repository.update(user_id, {
            "plan": "free",
            "price": 0.0,
            "expires_at": None
        })

    def get_expiring_soon(self, days: int = 7):
        return self.subscription_repository.get_expiring_subscription(days=days)
