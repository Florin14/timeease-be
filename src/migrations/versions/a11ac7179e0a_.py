"""empty message

Revision ID: a11ac7179e0a
Revises: 
Create Date: 2024-08-16 00:11:59.035826

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'a11ac7179e0a'
down_revision = None
branch_labels = None
depends_on = None

def upgrade_trigger():
    # in case of no search
    pass


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

    # manual section
    upgrade_trigger()


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
