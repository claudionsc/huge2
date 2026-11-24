from fastapi import Request

SUPPORTED_LOCALES = ("pt", "en")
DEFAULT_LOCALE = "pt"

TRANSLATIONS: dict[str, dict[str, str]] = {
    # Navigation
    "nav_home": {
        "pt": "Início",
        "en": "Home",
    },
    "nav_website_development": {
        "pt": "Criação de Sites",
        "en": "Website Development",
    },
    "nav_hosting": {
        "pt": "Hospedagem",
        "en": "Hosting",
    },
    "nav_professional_email": {
        "pt": "E-mail Profissional",
        "en": "Professional Email",
    },
    "nav_about": {
        "pt": "Sobre",
        "en": "About",
    },
    "nav_contact": {
        "pt": "Contato",
        "en": "Contact",
    },
    "nav_cases": {
        "pt": "Projetos",
        "en": "Projects",
    },

    # Hero
    "hero_location": {
        "pt": "São Paulo, BR · Global",
        "en": "São Paulo, BR · Worldwide",
    },
    "hero_title": {
        "pt": "Sua empresa merece uma presença digital profissional.",
        "en": "Your business deserves a professional digital presence.",
    },
    "hero_subtitle": {
        "pt": "Criamos sites profissionais, oferecemos hospedagem e configuramos e-mails personalizados para ajudar sua empresa a transmitir credibilidade e conquistar espaço na internet.",
        "en": "We create professional websites, provide hosting, and set up custom emails to help your business convey credibility and gain space on the internet.",
    },
    "hero_cta_primary": {
        "pt": "Solicitar Orçamento",
        "en": "Request a Quote",
    },
    "hero_cta_secondary": {
        "pt": "Conhecer Serviços",
        "en": "Explore Services",
    },
    "hero_scroll": {
        "pt": "Rolar",
        "en": "Scroll",
    },

    # Website Development
    "website_dev_title": {
        "pt": "Criação de Sites",
        "en": "Website Development",
    },
    "website_dev_subtitle": {
        "pt": "Sites profissionais que transmitem credibilidade e convertem visitantes em clientes.",
        "en": "Professional websites that convey credibility and convert visitors into customers.",
    },
    "landing_pages_title": {
        "pt": "Landing Pages",
        "en": "Landing Pages",
    },
    "landing_pages_desc": {
        "pt": "Páginas para apresentar serviços e divulgar ofertas com foco em conversão.",
        "en": "Pages to present services and promote offers with a focus on conversion.",
    },
    "landing_pages_features": {
        "pt": "Layout responsivo\nIntegração com WhatsApp\nFormulários de contato\nOtimizado para conversão",
        "en": "Responsive layout\nWhatsApp integration\nContact forms\nOptimized for conversion",
    },
    "institutional_sites_title": {
        "pt": "Sites Institucionais",
        "en": "Business Websites",
    },
    "institutional_sites_desc": {
        "pt": "Apresentação completa da sua empresa com páginas de serviços, contato e blog.",
        "en": "Complete presentation of your company with service pages, contact, and blog.",
    },
    "institutional_sites_features": {
        "pt": "Apresentação da empresa\nPáginas de serviços\nInformações de contato\nIntegração com WhatsApp\nEstrutura básica de SEO\nAdaptação para dispositivos móveis",
        "en": "Company presentation\nService pages\nContact information\nWhatsApp integration\nBasic SEO structure\nMobile responsive",
    },

    # Hosting & Maintenance
    "hosting_title": {
        "pt": "Hospedagem e Manutenção",
        "en": "Hosting & Maintenance",
    },
    "hosting_subtitle": {
        "pt": "Infraestrutura confiável e suporte técnico para seu site ficar sempre no ar.",
        "en": "Reliable infrastructure and technical support to keep your website always online.",
    },
    "hosting_features": {
        "pt": "Hospedagem de sites\nConfiguração de domínio e DNS\nCertificado SSL\nManutenção técnica\nAtualizações e ajustes\nMigração de hospedagem\nSuporte técnico",
        "en": "Website hosting\nDomain and DNS configuration\nSSL certificate\nTechnical maintenance\nUpdates and adjustments\nHosting migration\nTechnical support",
    },

    # Professional Email
    "email_title": {
        "pt": "E-mail Profissional",
        "en": "Professional Email",
    },
    "email_subtitle": {
        "pt": "E-mails com seu domínio para transmitir profissionalismo e confiança.",
        "en": "Emails with your domain to convey professionalism and trust.",
    },
    "email_examples": {
        "pt": "contato@suaempresa.com.br\nfinanceiro@suaempresa.com.br\nvendas@suaempresa.com.br",
        "en": "contact@yourcompany.com\nfinance@yourcompany.com\nsales@yourcompany.com",
    },
    "email_features": {
        "pt": "Configuração de contas\nConfiguração em computadores e dispositivos móveis\nAuxílio na configuração de clientes de e-mail\nGerenciamento de contas\nContratação independente da criação de site",
        "en": "Account setup\nSetup on computers and mobile devices\nEmail client configuration assistance\nAccount management\nIndependent hiring from website creation",
    },

    # Benefits
    "benefits_title": {
        "pt": "Por que ter uma presença digital profissional?",
        "en": "Why have a professional digital presence?",
    },
    "benefits_subtitle": {
        "pt": "Sua empresa ganha credibilidade, alcance e ferramentas para se comunicar melhor com clientes.",
        "en": "Your company gains credibility, reach, and tools to better communicate with customers.",
    },
    "benefit_credibility": {
        "pt": "Credibilidade",
        "en": "Credibility",
    },
    "benefit_credibility_desc": {
        "pt": "Um site profissional e e-mail com domínio próprio transmitem confiança imediata.",
        "en": "A professional website and custom domain email convey immediate trust.",
    },
    "benefit_reach": {
        "pt": "Alcance",
        "en": "Reach",
    },
    "benefit_reach_desc": {
        "pt": "Esteja disponível 24/7 para clientes em qualquer lugar, sem limitações geográficas.",
        "en": "Be available 24/7 for customers anywhere, without geographic limitations.",
    },
    "benefit_communication": {
        "pt": "Comunicação",
        "en": "Communication",
    },
    "benefit_communication_desc": {
        "pt": "Canais profissionais (site, e-mail, WhatsApp) facilitam o contato e agilizam negócios.",
        "en": "Professional channels (website, email, WhatsApp) facilitate contact and speed up business.",
    },
    "benefit_control": {
        "pt": "Controle",
        "en": "Control",
    },
    "benefit_control_desc": {
        "pt": "Você gerencia sua presença online sem depender apenas de redes sociais de terceiros.",
        "en": "You manage your online presence without relying solely on third-party social networks.",
    },

    # CTA
    "cta_title": {
        "pt": "Pronto para levar sua empresa para o próximo nível?",
        "en": "Ready to take your business to the next level?",
    },
    "cta_subtitle": {
        "pt": "Solicite um orçamento sem compromisso e descubra como podemos ajudar sua empresa a crescer na internet.",
        "en": "Request a no-obligation quote and discover how we can help your business grow online.",
    },
    "services_ready_title": {
        "pt": "Pronto para começar?",
        "en": "Ready to get started?",
    },
    "services_ready_subtitle": {
        "pt": "Entre em contato e vamos conversar sobre seu projeto.",
        "en": "Get in touch and let's talk about your project.",
    },
    "cta_primary": {
        "pt": "Solicitar Orçamento",
        "en": "Request a Quote",
    },
    "cta_secondary": {
        "pt": "Falar no WhatsApp",
        "en": "Chat on WhatsApp",
    },

    # About
    "about_title": {
        "pt": "Sobre a Alvi",
        "en": "About Alvi",
    },
    "about_description": {
        "pt": "A Alvi nasceu com o propósito de tornar a presença digital mais acessível para empresas e profissionais. Acreditamos que todo negócio merece uma apresentação profissional na internet e ferramentas digitais que facilitem sua comunicação com clientes.\n\nOferecemos soluções práticas em criação de sites, hospedagem, manutenção e e-mail profissional, acompanhando nossos clientes desde a configuração inicial até o suporte necessário para manter sua presença digital.",
        "en": "Alvi was born with the purpose of making digital presence more accessible for businesses and professionals. We believe every business deserves a professional presentation on the internet and digital tools that facilitate communication with clients.\n\nWe offer practical solutions in website creation, hosting, maintenance, and professional email, accompanying our clients from initial setup to the support needed to maintain their digital presence.",
    },
    "about_values_title": {
        "pt": "Nossos Valores",
        "en": "Our Values",
    },
    "about_team_title": {
        "pt": "A Equipe",
        "en": "The Team",
    },
    "value_accessibility": {
        "pt": "Acessibilidade",
        "en": "Accessibility",
    },
    "value_accessibility_desc": {
        "pt": "Tornamos a presença digital acessível para empresas de todos os portes.",
        "en": "We make digital presence accessible for businesses of all sizes.",
    },
    "value_simplicity": {
        "pt": "Simplicidade",
        "en": "Simplicity",
    },
    "value_simplicity_desc": {
        "pt": "Soluções práticas, sem complicação técnica desnecessária.",
        "en": "Practical solutions, without unnecessary technical complexity.",
    },
    "value_trust": {
        "pt": "Confiança",
        "en": "Trust",
    },
    "value_trust_desc": {
        "pt": "Entregamos o que prometemos, com transparência e suporte contínuo.",
        "en": "We deliver what we promise, with transparency and continuous support.",
    },
    "value_proximity": {
        "pt": "Proximidade",
        "en": "Proximity",
    },
    "value_proximity_desc": {
        "pt": "Acompanhamos de perto cada cliente, do início ao suporte contínuo.",
        "en": "We closely accompany each client, from start to ongoing support.",
    },

    # Contact
    "contact_title": {
        "pt": "Vamos conversar?",
        "en": "Let's talk?",
    },
    "contact_subtitle": {
        "pt": "Tem um projeto em mente ou precisa de ajuda com sua presença digital? Entre em contato conosco.",
        "en": "Have a project in mind or need help with your digital presence? Get in touch with us.",
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
        "pt": "Conte-nos sobre sua necessidade, prazo, orçamento ou apenas dê um olá...",
        "en": "Tell us about your needs, timeline, budget, or just say hi...",
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