from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.core.database import get_db
from app.core.i18n import t, get_locale_from_request, SUPPORTED_LOCALES, DEFAULT_LOCALE
from app.services.content_service import ContentService
from app.api.contact import router as contact_router

settings = get_settings()
router = APIRouter()

router.include_router(contact_router)

templates = Jinja2Templates(directory="app/templates")
templates.env.globals["t"] = t


def get_templates() -> Jinja2Templates:
    return templates


@router.get("/set-language/{lang}")
async def set_language(lang: str, request: Request, next: str | None = None):
    chosen_locale = lang.lower() if lang.lower() in SUPPORTED_LOCALES else DEFAULT_LOCALE
    redirect_url = next or request.headers.get("referer") or "/"
    if not redirect_url.startswith("/"):
        redirect_url = "/"
    response = RedirectResponse(url=redirect_url, status_code=303)
    response.set_cookie(key="locale", value=chosen_locale, max_age=365 * 24 * 3600, path="/")
    return response


@router.get("/", response_class=HTMLResponse)
async def home(
    request: Request,
    db: AsyncSession = Depends(get_db),
    templates: Jinja2Templates = Depends(get_templates),
):
    content = ContentService(db)
    locale = get_locale_from_request(request)

    service_categories = await content.get_service_categories(locale)
    products = await content.get_products(locale)
    case_studies = await content.get_case_studies(locale, limit=3)
    company = await content.get_company_info()
    values = await content.get_values(locale)
    about_sections = await content.get_about_sections(locale)

    for category in service_categories:
        category.services_list = await content.get_services_by_category(category.id, locale)

    response = templates.TemplateResponse(
        request,
        "index.html",
        {
            "service_categories": service_categories,
            "products": products,
            "case_studies": case_studies,
            "company": company,
            "values": values,
            "about_sections": about_sections,
            "locale": locale,
            "settings": settings,
        },
    )
    if "lang" in request.query_params or "locale" in request.query_params:
        response.set_cookie(key="locale", value=locale, max_age=365 * 24 * 3600, path="/")
    return response


@router.get("/services", response_class=HTMLResponse)
async def services_page(
    request: Request,
    db: AsyncSession = Depends(get_db),
    templates: Jinja2Templates = Depends(get_templates),
):
    content = ContentService(db)
    locale = get_locale_from_request(request)

    service_categories = await content.get_service_categories(locale)
    company = await content.get_company_info()

    for category in service_categories:
        category.services_list = await content.get_services_by_category(category.id, locale)

    response = templates.TemplateResponse(
        request,
        "services.html",
        {
            "service_categories": service_categories,
            "company": company,
            "locale": locale,
            "settings": settings,
        },
    )
    if "lang" in request.query_params or "locale" in request.query_params:
        response.set_cookie(key="locale", value=locale, max_age=365 * 24 * 3600, path="/")
    return response


@router.get("/portfolio", response_class=HTMLResponse)
async def portfolio_page(
    request: Request,
    db: AsyncSession = Depends(get_db),
    templates: Jinja2Templates = Depends(get_templates),
):
    content = ContentService(db)
    locale = get_locale_from_request(request)

    case_studies = await content.get_case_studies(locale)
    company = await content.get_company_info()

    response = templates.TemplateResponse(
        request,
        "portfolio.html",
        {
            "case_studies": case_studies,
            "company": company,
            "locale": locale,
            "settings": settings,
        },
    )
    if "lang" in request.query_params or "locale" in request.query_params:
        response.set_cookie(key="locale", value=locale, max_age=365 * 24 * 3600, path="/")
    return response


@router.get("/about", response_class=HTMLResponse)
async def about_page(
    request: Request,
    db: AsyncSession = Depends(get_db),
    templates: Jinja2Templates = Depends(get_templates),
):
    content = ContentService(db)
    locale = get_locale_from_request(request)

    company = await content.get_company_info()
    team_members = await content.get_team_members(locale)
    values = await content.get_values(locale)
    about_sections = await content.get_about_sections(locale)

    response = templates.TemplateResponse(
        request,
        "about.html",
        {
            "company": company,
            "team_members": team_members,
            "values": values,
            "about_sections": about_sections,
            "locale": locale,
            "settings": settings,
        },
    )
    if "lang" in request.query_params or "locale" in request.query_params:
        response.set_cookie(key="locale", value=locale, max_age=365 * 24 * 3600, path="/")
    return response


@router.get("/contact", response_class=HTMLResponse)
async def contact_page(
    request: Request,
    db: AsyncSession = Depends(get_db),
    templates: Jinja2Templates = Depends(get_templates),
):
    content = ContentService(db)
    locale = get_locale_from_request(request)

    service_categories = await content.get_service_categories(locale)
    company = await content.get_company_info()

    response = templates.TemplateResponse(
        request,
        "contact.html",
        {
            "service_categories": service_categories,
            "company": company,
            "locale": locale,
            "settings": settings,
        },
    )
    if "lang" in request.query_params or "locale" in request.query_params:
        response.set_cookie(key="locale", value=locale, max_age=365 * 24 * 3600, path="/")
    return response


@router.get("/health")
async def health_check():
    return {"status": "ok", "app": settings.app_name}
