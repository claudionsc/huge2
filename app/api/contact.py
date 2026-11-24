from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.config import get_settings
from app.core.i18n import t, get_locale_from_request

router = APIRouter(prefix="/api", tags=["contact"])
templates = Jinja2Templates(directory="app/templates")
templates.env.globals["t"] = t
settings = get_settings()


@router.post("/contact", response_class=HTMLResponse)
async def contact_form(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(""),
    service: str = Form(""),
    message: str = Form(...),
    website: str = Form(""),
    locale: str = Form(None),
    db: AsyncSession = Depends(get_db),
):
    active_locale = locale if locale in ("pt", "en") else get_locale_from_request(request)

    if website:
        return templates.TemplateResponse(
            request,
            "partials/contact_response.html",
            {"success": False, "error": t("contact_spam_error", active_locale)},
            status_code=400,
        )

    return templates.TemplateResponse(
        request,
        "partials/contact_response.html",
        {"success": True, "message": t("contact_success", active_locale)},
    )
