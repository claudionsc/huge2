from pydantic import BaseModel


class CaseStudyBase(BaseModel):
    id: str
    slug: str
    client_pt: str
    client_en: str
    title_pt: str
    title_en: str
    description_pt: str
    description_en: str
    challenge_pt: str
    challenge_en: str
    solution_pt: str
    solution_en: str
    results_pt: str
    results_en: str
    technologies_pt: str
    technologies_en: str
    image_url: str | None
    order: int
    is_visible: bool


class CaseStudyRead(CaseStudyBase):
    class Config:
        from_attributes = True