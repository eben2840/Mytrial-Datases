"""empty message

Revision ID: bafa78383f46
Revises: 995dbe68cac4
Create Date: 2022-08-17 16:06:07.115463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bafa78383f46'
down_revision = '995dbe68cac4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'person', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'person', type_='unique')
    # ### end Alembic commands ###
