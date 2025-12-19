import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Index

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    fullname = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False, index=True)
    updated_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)

    __table_args__ = [
        Index("idx_user_email", "email"),
        Index("idx_user_created_at", "created_at"),
        Index("idx_user_is_active", "is_active")
    ]

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email={self.email}, fullname={self.fullname})>"