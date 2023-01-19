"""Adicionando campo admin na tabela Usuario

Revision ID: 58e873df7fdf
Revises: f946328e7440
Create Date: 2023-01-19 17:57:39.909899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58e873df7fdf'
down_revision = 'f946328e7440'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
        batch_op.alter_column('matricula',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.alter_column('matricula',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.drop_column('id')

    # ### end Alembic commands ###
