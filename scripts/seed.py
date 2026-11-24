import asyncio
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import engine, async_session_maker
from app.models.base import Base
from app.models.service import ServiceCategory, Service
from app.models.product import Product
from app.models.case import CaseStudy
from app.models.company import CompanyInfo, TeamMember, Value
from app.models.about import AboutSection


async def create_tables():
    print("Tables in metadata:", list(Base.metadata.tables.keys()))
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created")


async def seed_data(db: AsyncSession):
    categories = [
        ServiceCategory(
            id="desenvolvimento",
            icon="Code2",
            name_pt="Desenvolvimento",
            name_en="Development",
            description_pt="Aplicações sob medida para web, mobile e desktop, do planejamento à entrega.",
            description_en="Tailor-made applications for web, mobile and desktop, from planning to delivery.",
            order=1,
            is_visible=True,
        ),
        ServiceCategory(
            id="produtos",
            icon="Rocket",
            name_pt="Produtos próprios",
            name_en="Own products",
            description_pt="Soluções de nicho e SaaS verticalizados com implantação rápida.",
            description_en="Niche solutions and verticalized SaaS with fast deployment.",
            order=2,
            is_visible=True,
        ),
        ServiceCategory(
            id="manutencao",
            icon="Wrench",
            name_pt="Manutenção",
            name_en="Maintenance",
            description_pt="Sustentação e alimentação contínua dos sistemas já entregues.",
            description_en="Ongoing support and data feeding for delivered systems.",
            order=3,
            is_visible=True,
        ),
    ]

    for cat in categories:
        db.add(cat)

    services = [
        Service(
            id="apps-sob-demanda",
            icon="MonitorSmartphone",
            category_id="desenvolvimento",
            title_pt="Aplicações sob demanda",
            title_en="On-demand applications",
            description_pt="Sistemas web, mobile e desktop desenvolvidos sob medida para a necessidade exata do seu negócio.",
            description_en="Web, mobile and desktop systems built exactly to your business needs.",
            features_pt="Definição de escopo e UX\nArquitetura escalável\nDeploy e sustentação",
            features_en="Scope definition and UX\nScalable architecture\nDeployment and support",
            order=1,
            is_visible=True,
        ),
        Service(
            id="sites-landing-pages",
            icon="Globe",
            category_id="desenvolvimento",
            title_pt="Sites institucionais & Landing Pages",
            title_en="Institutional sites & Landing Pages",
            description_pt="Presença digital profissional que apresenta sua empresa e converte visitantes.",
            description_en="A professional digital presence that presents your company and converts visitors.",
            features_pt="Design responsivo\nSEO e performance\nConteúdo gerenciável",
            features_en="Responsive design\nSEO and performance\nManageable content",
            order=2,
            is_visible=True,
        ),
        Service(
            id="ecommerce-saas",
            icon="ShoppingCart",
            category_id="desenvolvimento",
            title_pt="E-commerce & SaaS",
            title_en="E-commerce & SaaS",
            description_pt="Lojas virtuais e plataformas de assinatura robustas, seguras e preparadas para escalar.",
            description_en="Robust, secure and scalable online stores and subscription platforms.",
            features_pt="Pagamentos e carrinho\nPainel administrativo\nRelatórios e métricas",
            features_en="Payments and cart\nAdmin panel\nReports and metrics",
            order=3,
            is_visible=True,
        ),
        Service(
            id="desktop-windows-forms",
            icon="Monitor",
            category_id="desenvolvimento",
            title_pt="Aplicações desktop (Windows Forms)",
            title_en="Desktop apps (Windows Forms)",
            description_pt="Sistemas locais de alto desempenho com .NET, ideais para ambientes corporativos e de PDV.",
            description_en="High-performance local systems in .NET, ideal for corporate and POS environments.",
            features_pt="Integração com impressoras/leitores\nInstalação e atualização\nBanco de dados local",
            features_en="Printer/scanner integration\nInstall and update\nLocal database",
            order=4,
            is_visible=True,
        ),
        Service(
            id="pdv",
            icon="Store",
            category_id="desenvolvimento",
            title_pt="Frente de Caixa (PDV)",
            title_en="Point of Sale (POS)",
            description_pt="Soluções de frente de caixa ágeis e estáveis para o varejo e comércio.",
            description_en="Fast and stable point-of-sale solutions for retail and commerce.",
            features_pt="Venda e fechamento de caixa\nControle de estoque\nEmissão de notas",
            features_en="Sales and cash closing\nInventory control\nInvoice issuing",
            order=5,
            is_visible=True,
        ),
        Service(
            id="robo-licitacoes",
            icon="FileSearch",
            category_id="produtos",
            title_pt="Robô de licitações",
            title_en="Bidding robot",
            description_pt="Produto próprio que monitora e captura oportunidades de licitação automaticamente.",
            description_en="Own product that monitors and captures bidding opportunities automatically.",
            features_pt="Monitoramento contínuo\nAlertas de oportunidades\nPainel centralizado",
            features_en="Continuous monitoring\nOpportunity alerts\nCentralized dashboard",
            order=1,
            is_visible=True,
        ),
        Service(
            id="saas-verticalizados",
            icon="Layers",
            category_id="produtos",
            title_pt="SaaS verticalizados",
            title_en="Verticalized SaaS",
            description_pt="Plataformas prontas de nicho com implantação rápida e evolução contínua.",
            description_en="Ready-made niche platforms with fast onboarding and continuous evolution.",
            features_pt="Implantação rápida\nMulti-tenant\nEvolução contínua",
            features_en="Fast deployment\nMulti-tenant\nContinuous evolution",
            order=2,
            is_visible=True,
        ),
        Service(
            id="manutencao-sistemas",
            icon="ShieldCheck",
            category_id="manutencao",
            title_pt="Manutenção de sistemas",
            title_en="System maintenance",
            description_pt="Correções, melhorias e monitoramento para manter seus sistemas sempre no ar.",
            description_en="Fixes, improvements and monitoring to keep your systems always running.",
            features_pt="Correção de bugs\nAtualizações de segurança\nMonitoramento",
            features_en="Bug fixing\nSecurity updates\nMonitoring",
            order=1,
            is_visible=True,
        ),
        Service(
            id="alimentacao-sistemas",
            icon="Database",
            category_id="manutencao",
            title_pt="Alimentação de sistemas",
            title_en="System data feeding",
            description_pt="Inserção e gestão de dados para manter suas operações abastecidas e atualizadas.",
            description_en="Data entry and management to keep your operations supplied and up to date.",
            features_pt="Cadastro e migração\nAtualização de catálogo\nQualidade de dados",
            features_en="Registration and migration\nCatalog updates\nData quality",
            order=2,
            is_visible=True,
        ),
    ]

    for svc in services:
        db.add(svc)

    products = [
        Product(
            id="robo-licitacoes",
            icon="FileSearch",
            title_pt="Robô de Licitações",
            title_en="Bidding Robot",
            description_pt="Monitora e captura oportunidades de licitação automaticamente em portais públicos.",
            description_en="Monitors and captures bidding opportunities automatically from public portals.",
            features_pt="Monitoramento 24/7 de portais\nAlertas por e-mail/WhatsApp\nPainel centralizado de oportunidades\nFiltros por região/valor/categoria\nHistórico de editais",
            features_en="24/7 portal monitoring\nEmail/WhatsApp alerts\nCentralized opportunity dashboard\nFilters by region/value/category\nBid history",
            status_pt="Em produção",
            status_en="In production",
            link="/produtos/robo-licitacoes",
            order=1,
            is_visible=True,
        ),
        Product(
            id="saas-gestao-clinicas",
            icon="HeartPulse",
            title_pt="SaaS Gestão de Clínicas",
            title_en="Clinic Management SaaS",
            description_pt="Plataforma completa para gestão de clínicas e consultórios médicos.",
            description_en="Complete platform for clinic and medical office management.",
            features_pt="Agendamento online\nProntuário eletrônico\nTelemedicina integrada\nGestão financeira\nRelatórios gerenciais",
            features_en="Online scheduling\nElectronic health records\nIntegrated telemedicine\nFinancial management\nManagement reports",
            status_pt="Beta",
            status_en="Beta",
            link="/produtos/saas-clinicas",
            order=2,
            is_visible=True,
        ),
    ]

    for prod in products:
        db.add(prod)

    cases = [
        CaseStudy(
            id="case-ecommerce-moda",
            slug="ecommerce-moda",
            client_pt="Marca de Moda Nacional",
            client_en="National Fashion Brand",
            title_pt="E-commerce de Moda com 300% de Crescimento",
            title_en="Fashion E-commerce with 300% Growth",
            description_pt="Desenvolvimento de plataforma e-commerce completa para marca de moda com integração ERP, marketplace e logística.",
            description_en="Development of complete e-commerce platform for fashion brand with ERP, marketplace and logistics integration.",
            challenge_pt="Migração de plataforma legada sem downtime. Integração complexa com ERP e múltiplos marketplaces. Necessidade de escalar para Black Friday.",
            challenge_en="Legacy platform migration without downtime. Complex ERP and multiple marketplace integration. Need to scale for Black Friday.",
            solution_pt="Arquitetura headless com Next.js + FastAPI. Microserviços para pedidos, pagamentos e estoque. Cache inteligente e CDN global.",
            solution_en="Headless architecture with Next.js + FastAPI. Microservices for orders, payments and inventory. Smart caching and global CDN.",
            results_pt="300% aumento em conversão\n99.9% uptime na Black Friday\nRedução de 60% no tempo de carregamento\nIntegração 5 marketplaces",
            results_en="300% conversion increase\n99.9% uptime on Black Friday\n60% load time reduction\n5 marketplace integrations",
            technologies_pt="Next.js, FastAPI, PostgreSQL, Redis, Docker, AWS, Kubernetes",
            technologies_en="Next.js, FastAPI, PostgreSQL, Redis, Docker, AWS, Kubernetes",
            image_url="/images/cases/ecommerce-moda.jpg",
            order=1,
            is_visible=True,
        ),
        CaseStudy(
            id="case-pdv-varejo",
            slug="pdv-varejo",
            client_pt="Rede de Supermercados",
            client_en="Supermarket Chain",
            title_pt="Sistema PDV para 50+ Lojas",
            title_en="POS System for 50+ Stores",
            description_pt="Sistema de frente de caixa robusto com gestão de estoque centralizada, emissão fiscal e integração contábil.",
            description_en="Robust POS system with centralized inventory management, fiscal invoice issuing and accounting integration.",
            challenge_pt="Substituição de sistema legado em 50 lojas simultâneas. Conformidade fiscal (NF-e, NFC-e, SAT). Operação offline resiliente.",
            challenge_en="Legacy system replacement across 50 stores simultaneously. Fiscal compliance (NF-e, NFC-e, SAT). Resilient offline operation.",
            solution_pt="Aplicação Windows Forms .NET 8 com sincronização assíncrona. Banco local SQLite + sync para SQL Server central. Emissão fiscal nativa.",
            solution_en=".NET 8 Windows Forms app with async sync. Local SQLite DB + sync to central SQL Server. Native fiscal issuing.",
            results_pt="Zero falhas na migração\n100% conformidade fiscal\nOperação offline 100% funcional\nRedução 40% tempo checkout",
            results_en="Zero migration failures\n100% fiscal compliance\n100% functional offline operation\n40% checkout time reduction",
            technologies_pt=".NET 8, Windows Forms, SQLite, SQL Server, Dapper, Hangfire",
            technologies_en=".NET 8, Windows Forms, SQLite, SQL Server, Dapper, Hangfire",
            image_url="/images/cases/pdv-varejo.jpg",
            order=2,
            is_visible=True,
        ),
        CaseStudy(
            id="case-automacao-industrial",
            slug="automacao-industrial",
            client_pt="Indústria Automotiva",
            client_en="Automotive Industry",
            title_pt="Automação de Linha de Produção",
            title_en="Production Line Automation",
            description_pt="Automação de processos industriais com integração PLC, MES e dashboards em tempo real.",
            description_en="Industrial process automation with PLC, MES integration and real-time dashboards.",
            challenge_pt="Integração de equipamentos legados (PLC Siemens/Allen-Bradley). Coleta de dados em tempo real. Dashboard para gestão.",
            challenge_en="Integration of legacy equipment (Siemens/Allen-Bradley PLCs). Real-time data collection. Management dashboard.",
            solution_pt="Middleware OPC UA + Node-RED para coleta. API FastAPI para agregação. Dashboard React com WebSockets tempo real.",
            solution_en="OPC UA middleware + Node-RED for collection. FastAPI API for aggregation. React dashboard with real-time WebSockets.",
            results_pt="Redução 25% tempo setup\nVisibilidade 100% OEE\nAlertas preditivos manutenção\nROI 8 meses",
            results_en="25% setup time reduction\n100% OEE visibility\nPredictive maintenance alerts\n8-month ROI",
            technologies_pt="Python, FastAPI, OPC UA, Node-RED, React, WebSockets, InfluxDB, Grafana",
            technologies_en="Python, FastAPI, OPC UA, Node-RED, React, WebSockets, InfluxDB, Grafana",
            image_url="/images/cases/automacao-industrial.jpg",
            order=3,
            is_visible=True,
        ),
    ]

    for case in cases:
        db.add(case)

    company = CompanyInfo(
        id=1,
        name="ALVI",
        tagline_pt="Transformamos ideias em produtos digitais escaláveis",
        tagline_en="We turn ideas into scalable digital products",
        description_pt="Somos uma software house especializada em desenvolvimento de aplicações web, mobile e desktop, automações, produtos próprios e manutenção de sistemas. Atendemos do planejamento à entrega contínua.",
        description_en="We are a software house specialized in web, mobile and desktop application development, automation, own products and system maintenance. We serve from planning to continuous delivery.",
        email="contato@alvi.com.br",
        phone="+55 11 99999-9999",
        whatsapp="+5511999999999",
        whatsapp_link="https://wa.me/5511999999999",
        address_pt="São Paulo, SP - Brasil",
        address_en="São Paulo, SP - Brazil",
        instagram_url="https://instagram.com/alvi",
        linkedin_url="https://linkedin.com/company/alvi",
        facebook_url="https://facebook.com/alvi",
    )
    db.add(company)

    team = [
        TeamMember(
            id="founder",
            name="Claudio Silva",
            role_pt="Fundador & CEO",
            role_en="Founder & CEO",
            bio_pt="Mais de 15 anos desenvolvendo software para empresas de todos os portes. Especialista em arquitetura de sistemas, automação e produtos digitais.",
            bio_en="15+ years developing software for companies of all sizes. Specialist in system architecture, automation and digital products.",
            image_url="/images/team/claudio.jpg",
            order=1,
            is_visible=True,
        ),
    ]

    for member in team:
        db.add(member)

    values = [
        Value(
            id="qualidade",
            icon="ShieldCheck",
            title_pt="Qualidade Técnica",
            title_en="Technical Quality",
            description_pt="Código limpo, testável e documentado. Não entregamos dívida técnica.",
            description_en="Clean, testable, documented code. We don't deliver technical debt.",
            order=1,
            is_visible=True,
        ),
        Value(
            id="parceria",
            icon="Handshake",
            title_pt="Parceria Real",
            title_en="Real Partnership",
            description_pt="Trabalhamos como extensão do seu time. Seu sucesso é o nosso sucesso.",
            description_en="We work as an extension of your team. Your success is our success.",
            order=2,
            is_visible=True,
        ),
        Value(
            id="entrega",
            icon="Rocket",
            title_pt="Entrega Contínua",
            title_en="Continuous Delivery",
            description_pt="Metodologias ágeis, deploy automatizado, feedback rápido. Valor entregue toda sprint.",
            description_en="Agile methodologies, automated deploy, fast feedback. Value delivered every sprint.",
            order=3,
            is_visible=True,
        ),
        Value(
            id="transparencia",
            icon="Eye",
            title_pt="Transparência Total",
            title_en="Total Transparency",
            description_pt="Processos abertos, métricas visíveis, comunicação honesta. Sem surpresas.",
            description_en="Open processes, visible metrics, honest communication. No surprises.",
            order=4,
            is_visible=True,
        ),
    ]

    for val in values:
        db.add(val)

    about_sections = [
        AboutSection(
            id="historia",
            title_pt="Nossa História",
            title_en="Our Story",
            subtitle_pt="Como tudo começou",
            subtitle_en="How it all started",
            content_pt="A ALVI nasceu da vontade de criar software que realmente resolve problemas. Começamos pequenos, atendendo negócios locais, e crescemos mantendo a essência: qualidade técnica e parceria real. Hoje atendemos clientes em todo o Brasil, de startups a grandes corporações.",
            content_en="ALVI was born from the desire to create software that truly solves problems. We started small, serving local businesses, and grew while keeping our essence: technical quality and real partnership. Today we serve clients across Brazil, from startups to large corporations.",
            image_url="/images/about/historia.jpg",
            order=1,
            is_visible=True,
        ),
        AboutSection(
            id="missao",
            title_pt="Missão & Visão",
            title_en="Mission & Vision",
            subtitle_pt="O que nos move",
            subtitle_en="What drives us",
            content_pt="Nossa missão é democratizar tecnologia de ponta para empresas brasileiras. Queremos ser a melhor software house do Brasil, reconhecida pela excelência técnica e pelo impacto real nos negócios dos nossos clientes.",
            content_en="Our mission is to democratize cutting-edge technology for Brazilian companies. We want to be the best software house in Brazil, recognized for technical excellence and real impact on our clients' businesses.",
            image_url="/images/about/missao.jpg",
            order=2,
            is_visible=True,
        ),
    ]

    for section in about_sections:
        db.add(section)

    await db.commit()
    print("Seed data inserted successfully!")


async def main():
    await create_tables()

    async with async_session_maker() as db:
        await seed_data(db)

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())