"""add transaction_type field to Category table

Revision ID: c74a69013407
Revises: 4020c7e3ff7e
Create Date: 2024-08-04 10:47:44.345946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c74a69013407'
down_revision = '4020c7e3ff7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.add_column(sa.Column('transaction_type', sa.String(length=50), server_default='select', nullable=False))
        batch_op.create_index(batch_op.f('ix_category_transaction_type'), ['transaction_type'], unique=False)

    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.alter_column('loan_type',
               existing_type=sa.VARCHAR(length=30),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.alter_column('loan_type',
               existing_type=sa.VARCHAR(length=30),
               nullable=False)

    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_category_transaction_type'))
        batch_op.drop_column('transaction_type')

    # ### end Alembic commands ###