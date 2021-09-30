"""initial migrations

Revision ID: b897053a9aeb
Revises: 6bfad1593364
Create Date: 2021-09-30 11:32:39.478848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b897053a9aeb'
down_revision = '6bfad1593364'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('songs', sa.Column('artist', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('songs', 'artist')
    # ### end Alembic commands ###