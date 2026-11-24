from pydantic import BaseModel
from typing import Optional


class ServiceCategoryBase(BaseModel):
    id: str
    icon: str
    name_pt: str
    name_en: str
    description_pt: str
    description_en: str
    order: int
    is_visible: bool


class ServiceCategoryRead(ServiceCategoryBase):
    class Config:
        from_attributes = True


class ServiceBase(BaseModel):
    id: str
    icon: str
    category_id: str
    title_pt: str
    title_en: str
    description_pt: str
    description_en: str
    features_pt: str
    features_en: str
    order: int
    is_visible: bool


class ServiceRead(ServiceBase):
    class Config:
        from_attributes = True


class ServiceCategoryWithServices(ServiceCategoryRead):
    services: list[ServiceRead] = []