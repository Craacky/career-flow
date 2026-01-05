from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text, Index

from app.db.base import Base


class ParsingLog(Base):
    __tablename__ = "parsing_logs"

    id = Column(String(50), primary_key=True, index=True)
    source = Column(String(50), nullable=False, index=True)
    status = Column(String(50), nullable=False, index=True)

    jobs_found = Column(Integer, default=0, nullable=False)
    jobs_saved = Column(Integer, default=0, nullable=False)

    error_message = Column(Text, nullable=False)
    started_at = Column(DateTime, default=datetime.now, index=True, nullable=False)
    completed_at = Column(DateTime, nullable=True)

    __table_args__ = (
        Index('idx_parsing_log_source', 'source'),
        Index('idx_parsing_log_status', 'status'),
        Index('idx_parsing_log_started_at', 'started_at'),
    )

    def __repr__(self) -> str:
        return f"<ParsingLog(id={self.id}, source={self.source}, status={self.status})>"
