"""added breed column

Revision ID: 88602f709e2c
Revises: 
Create Date: 2021-05-11 08:56:06.374426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88602f709e2c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('puppies', sa.Column('breed', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('puppies', 'breed')
    # ### end Alembic commands ###
