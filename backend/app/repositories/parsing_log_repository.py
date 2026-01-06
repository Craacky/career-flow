from sqlalchemy.orm import Session
from app.models.parsing_log import ParsingLog
from app.repositories.base_repository import BaseRepository


class ParsingLogRepository(BaseRepository[ParsingLog]):
    def __init__(self, db: Session):
        super().__init__(ParsingLog, db)

    def get_latest(self, source: str | None = None) -> ParsingLog | None:
        query = self.db.query(ParsingLog)
        if source:
            query = query.filter(ParsingLog.source == source)

        return query.order_by(ParsingLog.started_at.desc()).first()

    def get_by_status(self, status: str, limit: int = 20) -> list[ParsingLog]:
        return (self.db.query(ParsingLog)
                .filter(ParsingLog.status == status)
                .order_by(ParsingLog.started_at.desc())
                .limit(limit)
                .all())

    def get_failed(self, limit: int = 20) -> list[ParsingLog]:
        return self.get_by_status("failed", limit=limit)

    def get_successful_by_source(self, source: str, limit: int = 20) -> list[ParsingLog]:
        return (self.db.query(ParsingLog).
                filter(ParsingLog.source == source, ParsingLog.status == "success")
                .order_by(ParsingLog.started_at.desc())
                .limit(limit)
                .all())

    def get_success_count(self) -> int:
        return self.db.query(ParsingLog).filter(ParsingLog.status == "success").count()

    def get_failed_count(self) -> int:
        return self.db.query(ParsingLog).filter(ParsingLog.status == "failed").count()

    def get_success_rate(self) -> float:
        total = self.count()
        if total == 0:
            return 0.0
        success = self.get_success_count()
        return (success / total) * 100
