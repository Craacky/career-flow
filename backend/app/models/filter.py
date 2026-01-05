from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index

from app.db.base import Base


class UserFilter(Base):
    __tablename__ = "user_filters"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    criteria = Column(String(255), nullable=False)

    created_at = Column(DateTime, default=datetime.now, index=True, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    __table_args__ = (
        Index('idx_filter_user_id', 'user_id'),
        Index('idx_filter_created_at', 'created_at'),
    )

    def __repr__(self) -> str:
        return f"<UserFilter(id={self.id}, user_id={self.user_id}, name={self.name})>"
