"""Initial Migration

Revision ID: 9054ade7ac20
Revises: 
Create Date: 2021-09-29 14:10:13.395703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9054ade7ac20'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
