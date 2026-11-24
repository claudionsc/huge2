from sqlalchemy import String, Text, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin


class Product(Base, TimestampMixin):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    icon: Mapped[str] = mapped_column(String(50), nullable=False)
    title_pt: Mapped[str] = mapped_column(String(150), nullable=False)
    title_en: Mapped[str] = mapped_column(String(150), nullable=False)
    description_pt: Mapped[str] = mapped_column(Text, nullable=False)
    description_en: Mapped[str] = mapped_column(Text, nullable=False)
    features_pt: Mapped[str] = mapped_column(Text, nullable=False)
    features_en: Mapped[str] = mapped_column(Text, nullable=False)
    status_pt: Mapped[str] = mapped_column(String(50), nullable=False)
    status_en: Mapped[str] = mapped_column(String(50), nullable=False)
    link: Mapped[str | None] = mapped_column(String(255), nullable=True)
    order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_visible: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    def title(self, locale: str = "pt") -> str:
        return getattr(self, f"title_{locale}", self.title_pt)

    def description(self, locale: str = "pt") -> str:
        return getattr(self, f"description_{locale}", self.description_pt)

    def features(self, locale: str = "pt") -> list[str]:
        features_text = getattr(self, f"features_{locale}", self.features_pt)
        return [f.strip() for f in features_text.split("\n") if f.strip()]

    def status(self, locale: str = "pt") -> str:
        return getattr(self, f"status_{locale}", self.status_pt)