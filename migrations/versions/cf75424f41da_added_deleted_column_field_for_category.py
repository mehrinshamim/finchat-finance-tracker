"""added deleted_column field for Category

Revision ID: cf75424f41da
Revises: c74a69013407
Create Date: 2024-08-04 13:10:40.945935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf75424f41da'
down_revision = 'c74a69013407'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deleted', sa.Boolean(), server_default='False', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.drop_column('deleted')

    # ### end Alembic commands ###
