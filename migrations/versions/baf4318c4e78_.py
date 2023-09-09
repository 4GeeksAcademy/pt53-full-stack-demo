"""empty message

Revision ID: baf4318c4e78
Revises: 3a5b5c7ca7fb
Create Date: 2023-08-30 23:50:09.364039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'baf4318c4e78'
down_revision = '3a5b5c7ca7fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stored_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(length=128), nullable=True),
    sa.Column('value', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('key')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stored_data')
    # ### end Alembic commands ###