from sqlalchemy import String, Text, Integer, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class ServiceCategory(Base, TimestampMixin):
    __tablename__ = "service_categories"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    icon: Mapped[str] = mapped_column(String(50), nullable=False)
    name_pt: Mapped[str] = mapped_column(String(100), nullable=False)
    name_en: Mapped[str] = mapped_column(String(100), nullable=False)
    description_pt: Mapped[str] = mapped_column(Text, nullable=False)
    description_en: Mapped[str] = mapped_column(Text, nullable=False)
    order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_visible: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    services: Mapped[list["Service"]] = relationship(
        "Service", back_populates="category", lazy="selectin", order_by="Service.order"
    )

    def name(self, locale: str = "pt") -> str:
        return getattr(self, f"name_{locale}", self.name_pt)

    def description(self, locale: str = "pt") -> str:
        return getattr(self, f"description_{locale}", self.description_pt)


class Service(Base, TimestampMixin):
    __tablename__ = "services"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    icon: Mapped[str] = mapped_column(String(50), nullable=False)
    category_id: Mapped[str] = mapped_column(
        String(50), ForeignKey("service_categories.id"), nullable=False
    )
    title_pt: Mapped[str] = mapped_column(String(150), nullable=False)
    title_en: Mapped[str] = mapped_column(String(150), nullable=False)
    description_pt: Mapped[str] = mapped_column(Text, nullable=False)
    description_en: Mapped[str] = mapped_column(Text, nullable=False)
    features_pt: Mapped[str] = mapped_column(Text, nullable=False)
    features_en: Mapped[str] = mapped_column(Text, nullable=False)
    order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_visible: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    category: Mapped["ServiceCategory"] = relationship("ServiceCategory", back_populates="services")

    def title(self, locale: str = "pt") -> str:
        return getattr(self, f"title_{locale}", self.title_pt)

    def description(self, locale: str = "pt") -> str:
        return getattr(self, f"description_{locale}", self.description_pt)

    def features(self, locale: str = "pt") -> list[str]:
        features_text = getattr(self, f"features_{locale}", self.features_pt)
        return [f.strip() for f in features_text.split("\n") if f.strip()]