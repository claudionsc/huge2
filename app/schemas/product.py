from pydantic import BaseModel


class ProductBase(BaseModel):
    id: str
    icon: str
    title_pt: str
    title_en: str
    description_pt: str
    description_en: str
    features_pt: str
    features_en: str
    status_pt: str
    status_en: str
    link: str | None
    order: int
    is_visible: bool


class ProductRead(ProductBase):
    class Config:
        from_attributes = True