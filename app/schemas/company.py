from pydantic import BaseModel


class CompanyInfoBase(BaseModel):
    id: int
    name: str
    tagline_pt: str
    tagline_en: str
    description_pt: str
    description_en: str
    email: str
    phone: str
    whatsapp: str
    whatsapp_link: str
    address_pt: str
    address_en: str
    instagram_url: str | None
    linkedin_url: str | None
    facebook_url: str | None


class CompanyInfoRead(CompanyInfoBase):
    class Config:
        from_attributes = True


class TeamMemberBase(BaseModel):
    id: str
    name: str
    role_pt: str
    role_en: str
    bio_pt: str
    bio_en: str
    image_url: str | None
    order: int
    is_visible: bool


class TeamMemberRead(TeamMemberBase):
    class Config:
        from_attributes = True


class ValueBase(BaseModel):
    id: str
    icon: str
    title_pt: str
    title_en: str
    description_pt: str
    description_en: str
    order: int
    is_visible: bool


class ValueRead(ValueBase):
    class Config:
        from_attributes = True