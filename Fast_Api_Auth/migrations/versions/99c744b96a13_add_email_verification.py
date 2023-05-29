"""add email verification

Revision ID: 99c744b96a13
Revises: 7e2ac4879582
Create Date: 2023-05-17 13:56:41.300813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99c744b96a13'
down_revision = '7e2ac4879582'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###