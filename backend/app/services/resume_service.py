from sqlalchemy.orm import Session

from app.models import Resume
from app.repositories.resume_repository import ResumeRepository


class ResumeService:
    def __init__(self, db: Session):
        self.db = db
        self.resume_repo = ResumeRepository(db)

    def save_resume(self, user_id: int, filename: str, file_path: str, extracted_text: str | None = None):
        return self.resume_repo.create({
            'user_id': user_id,
            'filename': filename,
            'file_path': file_path,
            'extracted_text': extracted_text
        })

    def get_user_resumes(self, user_id: int):
        return self.resume_repo.get_by_user(user_id)

    def get_latest_resume(self, user_id: int):
        return self.resume_repo.get_latest_by_user(user_id)

    def update_analysis(self, resume_id: int, analysis: str):
        return self.resume_repo.update(resume_id, {'analysis': analysis})

    def delete_resume(self, resume_id: int) -> bool:
        return self.resume_repo.delete(resume_id)

