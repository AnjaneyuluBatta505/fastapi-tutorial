"""category table

Revision ID: 61c84da4c884
Revises: 
Create Date: 2022-08-20 17:22:58.579108

"""
from alembic import op
from sqlalchemy import INTEGER, VARCHAR, Column, TIMESTAMP, func


# revision identifiers, used by Alembic.
revision = '61c84da4c884'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'category',
        Column('id', INTEGER, primary_key=True, auto_increment=True),
        Column('name', VARCHAR(30), nullable=False),
        Column('description', VARCHAR(255)),
        Column('timestamp', TIMESTAMP, server_default=func.now())
    )


def downgrade() -> None:
    op.drop_table('category')
