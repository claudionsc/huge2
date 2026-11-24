from sqlalchemy import String, Text, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin


class CompanyInfo(Base, TimestampMixin):
    __tablename__ = "company_info"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, default=1)
    name: Mapped[str] = mapped_column(String(100), nullable=False, default="ALVI")
    tagline_pt: Mapped[str] = mapped_column(String(255), nullable=False)
    tagline_en: Mapped[str] = mapped_column(String(255), nullable=False)
    description_pt: Mapped[str] = mapped_column(Text, nullable=False)
    description_en: Mapped[str] = mapped_column(Text, nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    phone: Mapped[str] = mapped_column(String(50), nullable=False)
    whatsapp: Mapped[str] = mapped_column(String(50), nullable=False)
    whatsapp_link: Mapped[str] = mapped_column(String(255), nullable=False)
    address_pt: Mapped[str] = mapped_column(String(255), nullable=False)
    address_en: Mapped[str] = mapped_column(String(255), nullable=False)
    instagram_url: Mapped[str | None] = mapped_column(String(255), nullable=True)
    linkedin_url: Mapped[str | None] = mapped_column(String(255), nullable=True)
    facebook_url: Mapped[str | None] = mapped_column(String(255), nullable=True)

    def tagline(self, locale: str = "pt") -> str:
        return getattr(self, f"tagline_{locale}", self.tagline_pt)

    def description(self, locale: str = "pt") -> str:
        return getattr(self, f"description_{locale}", self.description_pt)

    def address(self, locale: str = "pt") -> str:
        return getattr(self, f"address_{locale}", self.address_pt)


class TeamMember(Base, TimestampMixin):
    __tablename__ = "team_members"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    role_pt: Mapped[str] = mapped_column(String(100), nullable=False)
    role_en: Mapped[str] = mapped_column(String(100), nullable=False)
    bio_pt: Mapped[str] = mapped_column(Text, nullable=False)
    bio_en: Mapped[str] = mapped_column(Text, nullable=False)
    image_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_visible: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    def role(self, locale: str = "pt") -> str:
        return getattr(self, f"role_{locale}", self.role_pt)

    def bio(self, locale: str = "pt") -> str:
        return getattr(self, f"bio_{locale}", self.bio_pt)


class Value(Base, TimestampMixin):
    __tablename__ = "values"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    icon: Mapped[str] = mapped_column(String(50), nullable=False)
    title_pt: Mapped[str] = mapped_column(String(100), nullable=False)
    title_en: Mapped[str] = mapped_column(String(100), nullable=False)
    description_pt: Mapped[str] = mapped_column(Text, nullable=False)
    description_en: Mapped[str] = mapped_column(Text, nullable=False)
    order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_visible: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    def title(self, locale: str = "pt") -> str:
        return getattr(self, f"title_{locale}", self.title_pt)

    def description(self, locale: str = "pt") -> str:
        return getattr(self, f"description_{locale}", self.description_pt)