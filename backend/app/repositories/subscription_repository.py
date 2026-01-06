from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.models.subscription import Subscription
from app.repositories.base_repository import BaseRepository


class SubscriptionRepository(BaseRepository[Subscription]):
    def __init__(self, db: Session):
        super().__init__(Subscription, db)

    def get_by_user(self, user_id: int) -> Subscription | None:
        return (self.db.query(Subscription)
                .filter(Subscription.user_id == user_id)
                .first()
                )

    def is_active(self, user_id: int) -> bool:
        sub = self.get_by_user(user_id)
        return sub is not None and sub.is_active

    def is_pro(self, user_id: int) -> bool:
        sub = self.get_by_user(user_id)
        return sub is not None and sub.is_active and sub.plan == "pro"

    def get_active_subscription(self, limit: int = 100) -> list[Subscription] | None:
        return (self.db.query(Subscription)
                .filter(Subscription.plan == True)
                .limit(limit)
                .all()
                )

    def get_expiring_subscription(self, days: int = 7) -> list[Subscription]:
        now = datetime.now()
        future = now + timedelta(days=days)

        return (self.db.query(Subscription)
                .filter(Subscription.is_active == True,
                        Subscription.expires_at.between(now, future))
                .all()
                )
