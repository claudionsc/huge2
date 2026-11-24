from fastapi import Request

SUPPORTED_LOCALES = ("pt", "en")
DEFAULT_LOCALE = "pt"

TRANSLATIONS: dict[str, dict[str, str]] = {
    # Navigation
    "nav_services": {
        "pt": "Serviços",
        "en": "Services",
    },
    "nav_products": {
        "pt": "Produtos",
        "en": "Products",
    },
    "nav_cases": {
        "pt": "Cases",
        "en": "Cases",
    },
    "nav_about": {
        "pt": "Sobre",
        "en": "About",
    },
    "nav_contact": {
        "pt": "Contato",
        "en": "Contact",
    },
    "nav_cta": {
        "pt": "Fale Conosco",
        "en": "Let's Talk",
    },

    # Hero
    "hero_location": {
        "pt": "São Paulo, BR · Global",
        "en": "São Paulo, BR · Worldwide",
    },
    "hero_title": {
        "pt": "Transformamos ideias ambiciosas em produtos digitais escaláveis.",
        "en": "We turn ambitious ideas into scalable digital products.",
    },
    "hero_cta_primary": {
        "pt": "Iniciar Projeto",
        "en": "Start a Project",
    },
    "hero_cta_secondary": {
        "pt": "Explorar Serviços",
        "en": "Explore Services",
    },
    "hero_scroll": {
        "pt": "Rolar",
        "en": "Scroll",
    },

    # Philosophy
    "philosophy_title": {
        "pt": "Enxergamos o negócio por trás da tecnologia.",
        "en": "We see the business behind the technology.",
    },

    # Services
    "services_title": {
        "pt": "A estratégia. A construção. O caminho a seguir.",
        "en": "The thinking. The build. The way forward.",
    },
    "services_subtitle": {
        "pt": "Traga-nos o desafio: um produto a definir, um sistema a evoluir ou um projeto para colocar nos trilhos.",
        "en": "Bring us the challenge: a product to define, a system to improve or a project to get back on track.",
    },
    "services_ready_title": {
        "pt": "Pronto para iniciar seu projeto?",
        "en": "Ready to start your project?",
    },
    "services_ready_subtitle": {
        "pt": "Vamos conversar sobre seu desafio e encontrar o melhor caminho juntos.",
        "en": "Let's discuss your challenge and find the best way forward together.",
    },
    "services_ready_cta": {
        "pt": "Entrar em Contato",
        "en": "Get in Touch",
    },

    # Products
    "products_title": {
        "pt": "Ideias colocadas em prática.",
        "en": "Ideas, put to work.",
    },
    "products_subtitle": {
        "pt": "Produtos próprios nascidos de problemas reais que enfrentamos criando para clientes.",
        "en": "Our own products born from real problems we faced building for clients.",
    },
    "products_explore": {
        "pt": "Conhecer",
        "en": "Explore",
    },

    # Cases
    "cases_title": {
        "pt": "Experiências selecionadas do nosso portfólio.",
        "en": "Selected experience from our portfolio.",
    },
    "cases_subtitle": {
        "pt": "Desafios reais, soluções reais, resultados mensuráveis.",
        "en": "Real challenges, real solutions, measurable results.",
    },
    "cases_challenge": {
        "pt": "Desafio",
        "en": "Challenge",
    },
    "cases_solution": {
        "pt": "Solução",
        "en": "Solution",
    },
    "cases_results": {
        "pt": "Resultados",
        "en": "Results",
    },
    "cases_view_all": {
        "pt": "Ver Todos os Cases",
        "en": "View All Cases",
    },
    "cases_empty_title": {
        "pt": "Nenhum case ainda",
        "en": "No case studies yet",
    },
    "cases_empty_desc": {
        "pt": "Volte em breve para conferir nossos trabalhos mais recentes.",
        "en": "Check back soon for our latest work.",
    },

    # About
    "about_title": {
        "pt": "Por trás da ALVI",
        "en": "Behind ALVI",
    },
    "about_values_title": {
        "pt": "Nossos Valores",
        "en": "Our Values",
    },
    "about_team_title": {
        "pt": "A Equipe",
        "en": "The Team",
    },

    # CTA
    "cta_title": {
        "pt": "Pronto para construir algo extraordinário?",
        "en": "Ready to build something remarkable?",
    },
    "cta_subtitle": {
        "pt": "Traga-nos seu desafio. Nós entregamos a estratégia, a engenharia e a parceria para torná-lo realidade.",
        "en": "Bring us your challenge. We'll bring the strategy, engineering, and partnership to make it happen.",
    },
    "cta_primary": {
        "pt": "Iniciar Conversa",
        "en": "Start a Conversation",
    },
    "cta_secondary": {
        "pt": "Conhecer Nosso Trabalho",
        "en": "See Our Work",
    },

    # Contact
    "contact_title": {
        "pt": "Vamos trabalhar juntos.",
        "en": "Let's work together.",
    },
    "contact_subtitle": {
        "pt": "Tem um projeto em mente? Vamos conversar sobre como podemos ajudar a dar vida às suas ideias.",
        "en": "Have a project in mind? Let's discuss how we can help bring your ideas to life.",
    },
    "contact_form_title": {
        "pt": "Enviar uma Mensagem",
        "en": "Send a Message",
    },
    "contact_name": {
        "pt": "Nome *",
        "en": "Name *",
    },
    "contact_name_placeholder": {
        "pt": "Seu nome",
        "en": "Your name",
    },
    "contact_email": {
        "pt": "E-mail *",
        "en": "Email *",
    },
    "contact_email_placeholder": {
        "pt": "seu@email.com",
        "en": "your@email.com",
    },
    "contact_phone": {
        "pt": "Telefone",
        "en": "Phone",
    },
    "contact_phone_placeholder": {
        "pt": "+55 11 99999-9999",
        "en": "+55 11 99999-9999",
    },
    "contact_service": {
        "pt": "Serviço de Interesse",
        "en": "Service of Interest",
    },
    "contact_service_select": {
        "pt": "Selecione um serviço",
        "en": "Select a service",
    },
    "contact_service_other": {
        "pt": "Outro / Dúvida Geral",
        "en": "Other / General Inquiry",
    },
    "contact_message": {
        "pt": "Mensagem *",
        "en": "Message *",
    },
    "contact_message_placeholder": {
        "pt": "Conte-nos sobre seu projeto, prazos, orçamento ou apenas dê um olá...",
        "en": "Tell us about your project, timeline, budget, or just say hi...",
    },
    "contact_send": {
        "pt": "Enviar Mensagem",
        "en": "Send Message",
    },
    "contact_sending": {
        "pt": "Enviando...",
        "en": "Sending...",
    },
    "contact_required": {
        "pt": "* Campos obrigatórios",
        "en": "* Required fields",
    },
    "contact_direct": {
        "pt": "Contato Direto",
        "en": "Direct Contact",
    },
    "contact_email_label": {
        "pt": "E-mail",
        "en": "Email",
    },
    "contact_whatsapp_label": {
        "pt": "WhatsApp",
        "en": "WhatsApp",
    },
    "contact_location": {
        "pt": "Localização",
        "en": "Location",
    },
    "contact_follow": {
        "pt": "Siga-nos",
        "en": "Follow Us",
    },
    "contact_success": {
        "pt": "Obrigado! Entraremos em contato em breve.",
        "en": "Thank you! We will get in touch shortly.",
    },
    "contact_spam_error": {
        "pt": "Spam detectado.",
        "en": "Spam detected.",
    },

    # Footer
    "footer_company": {
        "pt": "Empresa",
        "en": "Company",
    },
    "footer_services": {
        "pt": "Serviços",
        "en": "Services",
    },
    "footer_contact": {
        "pt": "Contato",
        "en": "Contact",
    },
    "footer_about_us": {
        "pt": "Sobre Nós",
        "en": "About Us",
    },
    "footer_case_studies": {
        "pt": "Cases de Sucesso",
        "en": "Case Studies",
    },
    "footer_rights": {
        "pt": "Todos os direitos reservados.",
        "en": "All rights reserved.",
    },
    "footer_terms": {
        "pt": "Termos",
        "en": "Terms",
    },
    "footer_privacy": {
        "pt": "Privacidade",
        "en": "Privacy",
    },
    "footer_cookies": {
        "pt": "Cookies",
        "en": "Cookies",
    },
}


def t(key: str, locale: str = DEFAULT_LOCALE) -> str:
    """Returns the translation for key in given locale, falling back to pt or key."""
    entry = TRANSLATIONS.get(key)
    if not entry:
        return key
    return entry.get(locale, entry.get(DEFAULT_LOCALE, key))


def get_locale_from_request(request: Request) -> str:
    """Determines active locale from query param (?lang= or ?locale=), cookie or Accept-Language."""
    # 1. Query parameter
    lang_param = request.query_params.get("lang") or request.query_params.get("locale")
    if lang_param and lang_param.lower() in SUPPORTED_LOCALES:
        return lang_param.lower()

    # 2. Cookie
    cookie_lang = request.cookies.get("locale")
    if cookie_lang and cookie_lang.lower() in SUPPORTED_LOCALES:
        return cookie_lang.lower()

    # 3. Accept-Language header
    accept_lang = request.headers.get("accept-language", "").lower()
    if accept_lang:
        # Check if english is preferred
        pt_pos = accept_lang.find("pt")
        en_pos = accept_lang.find("en")
        if en_pos != -1 and (pt_pos == -1 or en_pos < pt_pos):
            return "en"

    return DEFAULT_LOCALE
