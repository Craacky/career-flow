from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey, String, Text, DateTime, Index

from app.db.base import Base


class Resume(Base):
    __tablename__ = "resume"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete="CASCADE"), nullable=False, index=True)
    filename = Column(String(255), nullable=False)
    filepath = Column(String(500), nullable=False)

    extracted_text = Column(Text, nullable=True)
    analysis = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.now, index=True, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    __table_args__ = (
        Index('idx_resume_user_id', 'user_id'),
        Index('idx_resume_created_at', 'created_at'),
    )

    def __repr__(self) -> str:
        return f"<Resume(id={self.id}, user_id={self.user_id}, file={self.filename})>"
