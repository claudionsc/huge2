from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.service import ServiceCategory, Service
from app.models.product import Product
from app.models.case import CaseStudy
from app.models.company import CompanyInfo, TeamMember, Value
from app.models.about import AboutSection


class ContentService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_service_categories(self, locale: str = "pt") -> list[ServiceCategory]:
        stmt = (
            select(ServiceCategory)
            .where(ServiceCategory.is_visible == True)
            .order_by(ServiceCategory.order)
        )
        result = await self.db.execute(stmt)
        return list(result.scalars().all())

    async def get_services_by_category(self, category_id: str, locale: str = "pt") -> list[Service]:
        stmt = (
            select(Service)
            .where(Service.category_id == category_id, Service.is_visible == True)
            .order_by(Service.order)
        )
        result = await self.db.execute(stmt)
        return list(result.scalars().all())

    async def get_all_services(self, locale: str = "pt") -> list[Service]:
        stmt = select(Service).where(Service.is_visible == True).order_by(Service.order)
        result = await self.db.execute(stmt)
        return list(result.scalars().all())

    async def get_products(self, locale: str = "pt") -> list[Product]:
        stmt = select(Product).where(Product.is_visible == True).order_by(Product.order)
        result = await self.db.execute(stmt)
        return list(result.scalars().all())

    async def get_case_studies(self, locale: str = "pt", limit: int | None = None) -> list[CaseStudy]:
        stmt = select(CaseStudy).where(CaseStudy.is_visible == True).order_by(CaseStudy.order)
        if limit:
            stmt = stmt.limit(limit)
        result = await self.db.execute(stmt)
        return list(result.scalars().all())

    async def get_company_info(self) -> CompanyInfo | None:
        stmt = select(CompanyInfo).where(CompanyInfo.id == 1)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def get_team_members(self, locale: str = "pt") -> list[TeamMember]:
        stmt = select(TeamMember).where(TeamMember.is_visible == True).order_by(TeamMember.order)
        result = await self.db.execute(stmt)
        return list(result.scalars().all())

    async def get_values(self, locale: str = "pt") -> list[Value]:
        stmt = select(Value).where(Value.is_visible == True).order_by(Value.order)
        result = await self.db.execute(stmt)
        return list(result.scalars().all())

    async def get_about_sections(self, locale: str = "pt") -> list[AboutSection]:
        stmt = select(AboutSection).where(AboutSection.is_visible == True).order_by(AboutSection.order)
        result = await self.db.execute(stmt)
        return list(result.scalars().all())