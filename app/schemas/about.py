from pydantic import BaseModel


class AboutSectionBase(BaseModel):
    id: str
    title_pt: str
    title_en: str
    subtitle_pt: str
    subtitle_en: str
    content_pt: str
    content_en: str
    image_url: str | None
    order: int
    is_visible: bool


class AboutSectionRead(AboutSectionBase):
    class Config:
        from_attributes = True