"""empty message

Revision ID: 222a82f72833
Revises: 
Create Date: 2021-12-18 22:08:50.188560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '222a82f72833'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=200), nullable=True),
    sa.Column('page_url', sa.String(length=200), nullable=True),
    sa.Column('image_url', sa.String(length=200), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('search',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('search_name', sa.String(length=200), nullable=True),
    sa.Column('created_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('search')
    op.drop_table('product')
    # ### end Alembic commands ###
