from sqlalchemy import String, Text, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin


class CaseStudy(Base, TimestampMixin):
    __tablename__ = "case_studies"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    slug: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    client_pt: Mapped[str] = mapped_column(String(150), nullable=False)
    client_en: Mapped[str] = mapped_column(String(150), nullable=False)
    title_pt: Mapped[str] = mapped_column(String(200), nullable=False)
    title_en: Mapped[str] = mapped_column(String(200), nullable=False)
    description_pt: Mapped[str] = mapped_column(Text, nullable=False)
    description_en: Mapped[str] = mapped_column(Text, nullable=False)
    challenge_pt: Mapped[str] = mapped_column(Text, nullable=False)
    challenge_en: Mapped[str] = mapped_column(Text, nullable=False)
    solution_pt: Mapped[str] = mapped_column(Text, nullable=False)
    solution_en: Mapped[str] = mapped_column(Text, nullable=False)
    results_pt: Mapped[str] = mapped_column(Text, nullable=False)
    results_en: Mapped[str] = mapped_column(Text, nullable=False)
    technologies_pt: Mapped[str] = mapped_column(Text, nullable=False)
    technologies_en: Mapped[str] = mapped_column(Text, nullable=False)
    image_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_visible: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    def client(self, locale: str = "pt") -> str:
        return getattr(self, f"client_{locale}", self.client_pt)

    def title(self, locale: str = "pt") -> str:
        return getattr(self, f"title_{locale}", self.title_pt)

    def description(self, locale: str = "pt") -> str:
        return getattr(self, f"description_{locale}", self.description_pt)

    def challenge(self, locale: str = "pt") -> str:
        return getattr(self, f"challenge_{locale}", self.challenge_pt)

    def solution(self, locale: str = "pt") -> str:
        return getattr(self, f"solution_{locale}", self.solution_pt)

    def results(self, locale: str = "pt") -> str:
        return getattr(self, f"results_{locale}", self.results_pt)

    def technologies(self, locale: str = "pt") -> list[str]:
        tech_text = getattr(self, f"technologies_{locale}", self.technologies_pt)
        return [t.strip() for t in tech_text.split(",") if t.strip()]