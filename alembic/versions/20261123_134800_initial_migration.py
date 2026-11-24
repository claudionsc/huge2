"""Initial migration

Revision ID: 20261123_134800
Revises: 
Create Date: 2026-11-23 13:48:00.000000

"""
from alembic import op
import sqlalchemy as sa


revision = '20261123_134800'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'service_categories',
        sa.Column('id', sa.String(50), nullable=False),
        sa.Column('icon', sa.String(50), nullable=False),
        sa.Column('name_pt', sa.String(100), nullable=False),
        sa.Column('name_en', sa.String(100), nullable=False),
        sa.Column('description_pt', sa.Text(), nullable=False),
        sa.Column('description_en', sa.Text(), nullable=False),
        sa.Column('order', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('is_visible', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_service_categories_order', 'service_categories', ['order'])

    op.create_table(
        'services',
        sa.Column('id', sa.String(50), nullable=False),
        sa.Column('icon', sa.String(50), nullable=False),
        sa.Column('category_id', sa.String(50), nullable=False),
        sa.Column('title_pt', sa.String(150), nullable=False),
        sa.Column('title_en', sa.String(150), nullable=False),
        sa.Column('description_pt', sa.Text(), nullable=False),
        sa.Column('description_en', sa.Text(), nullable=False),
        sa.Column('features_pt', sa.Text(), nullable=False),
        sa.Column('features_en', sa.Text(), nullable=False),
        sa.Column('order', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('is_visible', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['category_id'], ['service_categories.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_services_category_id', 'services', ['category_id'])
    op.create_index('ix_services_order', 'services', ['order'])

    op.create_table(
        'products',
        sa.Column('id', sa.String(50), nullable=False),
        sa.Column('icon', sa.String(50), nullable=False),
        sa.Column('title_pt', sa.String(150), nullable=False),
        sa.Column('title_en', sa.String(150), nullable=False),
        sa.Column('description_pt', sa.Text(), nullable=False),
        sa.Column('description_en', sa.Text(), nullable=False),
        sa.Column('features_pt', sa.Text(), nullable=False),
        sa.Column('features_en', sa.Text(), nullable=False),
        sa.Column('status_pt', sa.String(50), nullable=False),
        sa.Column('status_en', sa.String(50), nullable=False),
        sa.Column('link', sa.String(255), nullable=True),
        sa.Column('order', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('is_visible', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_products_order', 'products', ['order'])

    op.create_table(
        'case_studies',
        sa.Column('id', sa.String(50), nullable=False),
        sa.Column('slug', sa.String(100), nullable=False),
        sa.Column('client_pt', sa.String(150), nullable=False),
        sa.Column('client_en', sa.String(150), nullable=False),
        sa.Column('title_pt', sa.String(200), nullable=False),
        sa.Column('title_en', sa.String(200), nullable=False),
        sa.Column('description_pt', sa.Text(), nullable=False),
        sa.Column('description_en', sa.Text(), nullable=False),
        sa.Column('challenge_pt', sa.Text(), nullable=False),
        sa.Column('challenge_en', sa.Text(), nullable=False),
        sa.Column('solution_pt', sa.Text(), nullable=False),
        sa.Column('solution_en', sa.Text(), nullable=False),
        sa.Column('results_pt', sa.Text(), nullable=False),
        sa.Column('results_en', sa.Text(), nullable=False),
        sa.Column('technologies_pt', sa.Text(), nullable=False),
        sa.Column('technologies_en', sa.Text(), nullable=False),
        sa.Column('image_url', sa.String(500), nullable=True),
        sa.Column('order', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('is_visible', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('slug')
    )
    op.create_index('ix_case_studies_slug', 'case_studies', ['slug'], unique=True)
    op.create_index('ix_case_studies_order', 'case_studies', ['order'])

    op.create_table(
        'company_info',
        sa.Column('id', sa.Integer(), nullable=False, server_default='1'),
        sa.Column('name', sa.String(100), nullable=False, server_default='HUGE'),
        sa.Column('tagline_pt', sa.String(255), nullable=False),
        sa.Column('tagline_en', sa.String(255), nullable=False),
        sa.Column('description_pt', sa.Text(), nullable=False),
        sa.Column('description_en', sa.Text(), nullable=False),
        sa.Column('email', sa.String(150), nullable=False),
        sa.Column('phone', sa.String(50), nullable=False),
        sa.Column('whatsapp', sa.String(50), nullable=False),
        sa.Column('whatsapp_link', sa.String(255), nullable=False),
        sa.Column('address_pt', sa.String(255), nullable=False),
        sa.Column('address_en', sa.String(255), nullable=False),
        sa.Column('instagram_url', sa.String(255), nullable=True),
        sa.Column('linkedin_url', sa.String(255), nullable=True),
        sa.Column('facebook_url', sa.String(255), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'team_members',
        sa.Column('id', sa.String(50), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('role_pt', sa.String(100), nullable=False),
        sa.Column('role_en', sa.String(100), nullable=False),
        sa.Column('bio_pt', sa.Text(), nullable=False),
        sa.Column('bio_en', sa.Text(), nullable=False),
        sa.Column('image_url', sa.String(500), nullable=True),
        sa.Column('order', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('is_visible', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_team_members_order', 'team_members', ['order'])

    op.create_table(
        'values',
        sa.Column('id', sa.String(50), nullable=False),
        sa.Column('icon', sa.String(50), nullable=False),
        sa.Column('title_pt', sa.String(100), nullable=False),
        sa.Column('title_en', sa.String(100), nullable=False),
        sa.Column('description_pt', sa.Text(), nullable=False),
        sa.Column('description_en', sa.Text(), nullable=False),
        sa.Column('order', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('is_visible', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_values_order', 'values', ['order'])

    op.create_table(
        'about_sections',
        sa.Column('id', sa.String(50), nullable=False),
        sa.Column('title_pt', sa.String(200), nullable=False),
        sa.Column('title_en', sa.String(200), nullable=False),
        sa.Column('subtitle_pt', sa.Text(), nullable=False),
        sa.Column('subtitle_en', sa.Text(), nullable=False),
        sa.Column('content_pt', sa.Text(), nullable=False),
        sa.Column('content_en', sa.Text(), nullable=False),
        sa.Column('image_url', sa.String(500), nullable=True),
        sa.Column('order', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('is_visible', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_about_sections_order', 'about_sections', ['order'])


def downgrade() -> None:
    op.drop_index('ix_about_sections_order', table_name='about_sections')
    op.drop_table('about_sections')
    op.drop_index('ix_values_order', table_name='values')
    op.drop_table('values')
    op.drop_index('ix_team_members_order', table_name='team_members')
    op.drop_table('team_members')
    op.drop_table('company_info')
    op.drop_index('ix_case_studies_order', table_name='case_studies')
    op.drop_index('ix_case_studies_slug', table_name='case_studies')
    op.drop_table('case_studies')
    op.drop_index('ix_products_order', table_name='products')
    op.drop_table('products')
    op.drop_index('ix_services_order', table_name='services')
    op.drop_index('ix_services_category_id', table_name='services')
    op.drop_table('services')
    op.drop_index('ix_service_categories_order', table_name='service_categories')
    op.drop_table('service_categories')