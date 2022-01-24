"""empty message

Revision ID: 257a9874596a
Revises: 7b5df3c58fca
Create Date: 2021-12-21 20:57:24.115351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '257a9874596a'
down_revision = '7b5df3c58fca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.Text(), nullable=True),
    sa.Column('page_url', sa.Text(), nullable=True),
    sa.Column('image_url', sa.Text(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('clean_name', sa.Text(), nullable=True),
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