# HUGE2 - Software House Website

Modern, fullstack website for HUGE software house built with FastAPI, PostgreSQL, Jinja2, HTMX, and Tailwind CSS.

## Tech Stack

- **Backend**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL with SQLAlchemy 2.0 + Alembic migrations
- **Frontend**: Jinja2 templates (SSR) + HTMX + Alpine.js
- **Styling**: Tailwind CSS (via CDN)
- **Icons**: Inline SVG (Lucide-style)

## Project Structure

```
HUGE2/
├── app/
│   ├── api/           # API routes
│   ├── core/          # Config, database
│   ├── models/        # SQLAlchemy models
│   ├── schemas/       # Pydantic schemas
│   ├── services/      # Business logic
│   ├── templates/     # Jinja2 templates
│   │   └── partials/  # Reusable partials
│   ├── static/        # Static assets
│   └── main.py        # FastAPI app entry
├── alembic/           # Database migrations
├── scripts/           # Utility scripts
├── requirements.txt
├── pyproject.toml
└── .env.example
```

## Features

- **Single-page inspired design** (like apekon.com) with numbered sections
- **Dark theme** with gold/amber accent
- **Responsive** mobile-first design
- **SEO-friendly** server-side rendering
- **Interactive** with HTMX (no SPA complexity)
- **Content-driven** from PostgreSQL database
- **Multilingual ready** (PT/EN structure)
- **Contact form** with HTMX submission

## Sections

1. **Hero** - Statement + CTA
2. **Philosophy** - Company values
3. **Services** - Categorized services with features
4. **Products** - Own products showcase
5. **Cases** - Case studies with challenge/solution/results
6. **About** - Story, mission, team
7. **Contact** - Form + direct contact info

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL 14+
- uv (recommended) or pip

### Installation

```bash
# Clone and enter directory
cd HUGE2

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
# Edit .env with your database URL

# Run migrations
alembic upgrade head

# Seed database
python scripts/seed.py

# Start development server
uvicorn app.main:app --reload --port 8000
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql+asyncpg://postgres:postgres@localhost:5432/huge2` |
| `APP_NAME` | Application name | `HUGE` |
| `APP_HOST` | Host to bind | `0.0.0.0` |
| `APP_PORT` | Port to bind | `8000` |
| `DEBUG` | Debug mode | `true` |
| `SECRET_KEY` | Secret key for sessions | `dev-secret-key-change-in-production` |
| `TAILWIND_CDN` | Use Tailwind CDN | `true` |

## Database Schema

- `service_categories` - Service categories (Development, Products, Maintenance)
- `services` - Individual services linked to categories
- `products` - Own products showcase
- `case_studies` - Portfolio cases with challenge/solution/results
- `company_info` - Company details (single row)
- `team_members` - Team members
- `values` - Company values
- `about_sections` - About page sections

## Development

```bash
# Run with auto-reload
uvicorn app.main:app --reload

# Create new migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Run tests
pytest

# Format code
ruff format .
black .

# Lint
ruff check .
```

## Deployment

### Docker (recommended)

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN alembic upgrade head && python scripts/seed.py

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Production Checklist

- [ ] Set `DEBUG=false`
- [ ] Generate strong `SECRET_KEY`
- [ ] Use PostgreSQL with connection pooling
- [ ] Set up reverse proxy (nginx)
- [ ] Configure HTTPS
- [ ] Set up monitoring/logging
- [ ] Configure backup strategy

## License

MIT