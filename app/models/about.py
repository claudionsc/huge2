from sqlalchemy import String, Text, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin


class AboutSection(Base, TimestampMixin):
    __tablename__ = "about_sections"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    title_pt: Mapped[str] = mapped_column(String(200), nullable=False)
    title_en: Mapped[str] = mapped_column(String(200), nullable=False)
    subtitle_pt: Mapped[str] = mapped_column(Text, nullable=False)
    subtitle_en: Mapped[str] = mapped_column(Text, nullable=False)
    content_pt: Mapped[str] = mapped_column(Text, nullable=False)
    content_en: Mapped[str] = mapped_column(Text, nullable=False)
    image_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_visible: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    def title(self, locale: str = "pt") -> str:
        return getattr(self, f"title_{locale}", self.title_pt)

    def subtitle(self, locale: str = "pt") -> str:
        return getattr(self, f"subtitle_{locale}", self.subtitle_pt)

    def content(self, locale: str = "pt") -> str:
        return getattr(self, f"content_{locale}", self.content_pt)