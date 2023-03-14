"""empty message

Revision ID: 549793766e16
Revises: daa7a03c26d3
Create Date: 2023-03-13 17:42:38.223745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '549793766e16'
down_revision = 'daa7a03c26d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('promotion', schema=None) as batch_op:
        batch_op.alter_column('start_date',
               existing_type=sa.VARCHAR(),
               type_=sa.DateTime(),
               existing_nullable=True)
        batch_op.alter_column('end_date',
               existing_type=sa.VARCHAR(),
               type_=sa.DateTime(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('promotion', schema=None) as batch_op:
        batch_op.alter_column('end_date',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(),
               existing_nullable=True)
        batch_op.alter_column('start_date',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(),
               existing_nullable=True)

    # ### end Alembic commands ###
