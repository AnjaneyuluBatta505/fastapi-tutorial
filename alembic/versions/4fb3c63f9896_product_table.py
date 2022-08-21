"""product table

Revision ID: 4fb3c63f9896
Revises: 61c84da4c884
Create Date: 2022-08-20 17:57:13.574869

"""
from alembic import op
from sqlalchemy import INTEGER, VARCHAR, Column, TIMESTAMP, func, DECIMAL, ForeignKey


# revision identifiers, used by Alembic.
revision = '4fb3c63f9896'
down_revision = '61c84da4c884'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'product',
        Column('id', INTEGER, primary_key=True, auto_increment=True),
        Column('name', VARCHAR(30), nullable=False),
        Column('quantity', INTEGER),
        Column('price', DECIMAL),
        Column('category_id', INTEGER, ForeignKey('category.id', ), nullable=False),
        Column('timestamp', TIMESTAMP, server_default=func.now())
    )


def downgrade() -> None:
    op.drop_table('product')
