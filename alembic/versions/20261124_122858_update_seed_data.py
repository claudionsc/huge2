"""Update seed data for new services

Revision ID: 20261124_122858_update_seed_data
Revises: 20261123_134800
Create Date: 2026-11-24 12:28:58.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

revision = '20261124_122858_update_seed_data'
down_revision = '20261123_134800'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Update company_info
    op.execute("""
        UPDATE company_info SET
            tagline_pt = 'Sua presença digital profissional',
            tagline_en = 'Your professional digital presence',
            description_pt = 'A Alvi nasceu com o propósito de tornar a presença digital mais acessível para empresas e profissionais. Acreditamos que todo negócio merece uma apresentação profissional na internet e ferramentas digitais que facilitem sua comunicação com clientes. Oferecemos soluções práticas em criação de sites, hospedagem, manutenção e e-mail profissional, acompanhando nossos clientes desde a configuração inicial até o suporte necessário para manter sua presença digital.',
            description_en = 'Alvi was born with the purpose of making digital presence more accessible for businesses and professionals. We believe every business deserves a professional presentation on the internet and digital tools that facilitate communication with clients. We offer practical solutions in website creation, hosting, maintenance, and professional email, accompanying our clients from initial setup to the support needed to maintain their digital presence.'
        WHERE id = 1
    """)

    # Delete old service categories and services (we'll recreate them)
    op.execute("DELETE FROM services")
    op.execute("DELETE FROM service_categories")

    # Insert new service categories
    op.execute("""
        INSERT INTO service_categories (id, icon, name_pt, name_en, description_pt, description_en, "order", is_visible) VALUES
        ('website_development', 'globe', 'Criação de Sites', 'Website Development', 'Sites profissionais que transmitem credibilidade e convertem visitantes em clientes.', 'Professional websites that convey credibility and convert visitors into customers.', 1, 1),
        ('hosting', 'server', 'Hospedagem e Manutenção', 'Hosting & Maintenance', 'Infraestrutura confiável e suporte técnico para seu site ficar sempre no ar.', 'Reliable infrastructure and technical support to keep your website always online.', 2, 1),
        ('professional_email', 'mail', 'E-mail Profissional', 'Professional Email', 'E-mails com seu domínio para transmitir profissionalismo e confiança.', 'Emails with your domain to convey professionalism and trust.', 3, 1)
    """)

    # Insert new services
    op.execute("""
        INSERT INTO services (id, icon, category_id, title_pt, title_en, description_pt, description_en, features_pt, features_en, "order", is_visible) VALUES
        -- Landing Pages
        ('landing-pages', 'file-text', 'website_development', 'Landing Pages', 'Landing Pages', 'Páginas para apresentar serviços e divulgar ofertas com foco em conversão.', 'Pages to present services and promote offers with a focus on conversion.', 'Layout responsivo\nIntegração com WhatsApp\nFormulários de contato\nOtimizado para conversão', 'Responsive layout\nWhatsApp integration\nContact forms\nOptimized for conversion', 1, 1),
        -- Sites Institucionais
        ('institutional-sites', 'building', 'website_development', 'Sites Institucionais', 'Business Websites', 'Apresentação completa da sua empresa com páginas de serviços, contato e blog.', 'Complete presentation of your company with service pages, contact, and blog.', 'Apresentação da empresa\nPáginas de serviços\nInformações de contato\nIntegração com WhatsApp\nEstrutura básica de SEO\nAdaptação para dispositivos móveis', 'Company presentation\nService pages\nContact information\nWhatsApp integration\nBasic SEO structure\nMobile responsive', 2, 1),
        -- Hospedagem e Manutenção
        ('hosting-maintenance', 'hard-drive', 'hosting', 'Hospedagem e Manutenção', 'Hosting & Maintenance', 'Infraestrutura confiável e suporte técnico para seu site ficar sempre no ar.', 'Reliable infrastructure and technical support to keep your website always online.', 'Hospedagem de sites\nConfiguração de domínio e DNS\nCertificado SSL\nManutenção técnica\nAtualizações e ajustes\nMigração de hospedagem\nSuporte técnico', 'Website hosting\nDomain and DNS configuration\nSSL certificate\nTechnical maintenance\nUpdates and adjustments\nHosting migration\nTechnical support', 1, 1),
        -- E-mail Profissional
        ('professional-email', 'mail', 'professional_email', 'E-mail Profissional', 'Professional Email', 'E-mails com seu domínio para transmitir profissionalismo e confiança.', 'Emails with your domain to convey professionalism and trust.', 'Configuração de contas\nConfiguração em computadores e dispositivos móveis\nAuxílio na configuração de clientes de e-mail\nGerenciamento de contas\nContratação independente da criação de site', 'Account setup\nSetup on computers and mobile devices\nEmail client configuration assistance\nAccount management\nIndependent hiring from website creation', 1, 1)
    """)

    # Update values
    op.execute("DELETE FROM \"values\"")
    op.execute("""
        INSERT INTO "values" (id, icon, title_pt, title_en, description_pt, description_en, "order", is_visible) VALUES
        ('accessibility', 'users', 'Acessibilidade', 'Accessibility', 'Tornamos a presença digital acessível para empresas de todos os portes.', 'We make digital presence accessible for businesses of all sizes.', 1, 1),
        ('simplicity', 'zap', 'Simplicidade', 'Simplicity', 'Soluções práticas, sem complicação técnica desnecessária.', 'Practical solutions, without unnecessary technical complexity.', 2, 1),
        ('trust', 'shield', 'Confiança', 'Trust', 'Entregamos o que prometemos, com transparência e suporte contínuo.', 'We deliver what we promise, with transparency and continuous support.', 3, 1),
        ('proximity', 'heart', 'Proximidade', 'Proximity', 'Acompanhamos de perto cada cliente, do início ao suporte contínuo.', 'We closely accompany each client, from start to ongoing support.', 4, 1)
    """)

    # Update about_sections - we can keep the existing ones or update them
    op.execute("DELETE FROM about_sections")
    op.execute("""
        INSERT INTO about_sections (id, title_pt, title_en, subtitle_pt, subtitle_en, content_pt, content_en, "order", is_visible) VALUES
        ('nossa-historia', 'Nossa História', 'Our Story', 'Como tudo começou', 'How it all started', 'A Alvi nasceu da vontade de tornar a presença digital acessível para qualquer negócio. Começamos atendendo empresas locais que precisavam de um site profissional, hospedagem confiável e e-mail com domínio próprio. Hoje, continuamos com a mesma essência: simplicidade, confiança e proximidade.', 'Alvi was born from the desire to make digital presence accessible for any business. We started serving local businesses that needed a professional website, reliable hosting, and custom domain email. Today, we continue with the same essence: simplicity, trust, and proximity.', 1, 1),
        ('missao-visao', 'Missão e Visão', 'Mission & Vision', 'O que nos move', 'What drives us', 'Nossa missão é democratizar a presença digital profissional para empresas brasileiras. Queremos ser a escolha natural para quem busca criar seu site, hospedá-lo e ter e-mails profissionais, reconhecidos pela qualidade do atendimento e pela simplicidade das soluções.', 'Our mission is to democratize professional digital presence for Brazilian companies. We want to be the natural choice for those seeking to create their website, host it, and have professional emails, recognized for service quality and solution simplicity.', 2, 1)
    """)

    # Hide products and case studies (set is_visible = false)
    op.execute("UPDATE products SET is_visible = 0")
    op.execute("UPDATE case_studies SET is_visible = 0")


def downgrade() -> None:
    # Restore old data would be complex, so we just note it's not easily reversible
    pass