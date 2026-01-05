from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index, Float, Table, Text

from app.db.base import Base

job_favorites = Table(
    "job_favorites",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("job_id", Integer, ForeignKey("jobs.id"), primary_key=True),
)


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), index=True, nullable=False)
    company = Column(String(255), index=True, nullable=False)
    location = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    requirements = Column(Text, nullable=True)
    tech_stack = Column(String(1000), nullable=True)

    salary_min = Column(Float, nullable=True)
    salary_max = Column(Float, nullable=True)
    currency = Column(String(10), default="USD")

    url = Column(String(500), unique=True, nullable=False)
    source = Column(String(50), index=True, nullable=False)

    experience_level = Column(String(50), nullable=True)
    employment_level = Column(String(50), nullable=True)
    work_format = Column(String(50), nullable=True, index=True)

    published_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.now, index=True, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    __table_args__ = (
        Index('idx_job_source', 'source'),
        Index('idx_job_created_at', 'created_at'),
        Index('idx_job_experience_level', 'experience_level'),
        Index('idx_job_work_format', 'work_format'),
    )

    def __repr__(self) -> str:
        return f"<Job(id={self.id}, title={self.title}, company={self.company})>"
