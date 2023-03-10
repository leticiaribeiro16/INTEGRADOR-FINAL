"""Migração inicial

Revision ID: a8d6e144442c
Revises: 
Create Date: 2023-01-19 19:06:44.057367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8d6e144442c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('demanda',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('observacoes', sa.Text(), nullable=True),
    sa.Column('materia', sa.String(length=100), nullable=True),
    sa.Column('requistos', sa.Text(), nullable=True),
    sa.Column('vagas_matutino', sa.Float(), nullable=True),
    sa.Column('vagas_vespertino', sa.Float(), nullable=True),
    sa.Column('vagas_noturno', sa.Float(), nullable=True),
    sa.Column('vagas_flexivel', sa.Float(), nullable=True),
    sa.Column('bolsas_matutino', sa.Float(), nullable=True),
    sa.Column('bolsas_vespertino', sa.Float(), nullable=True),
    sa.Column('bolsas_noturno', sa.Float(), nullable=True),
    sa.Column('bolsas_flexivel', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('matricula', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('senha', sa.String(length=100), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    op.drop_table('demanda')
    # ### end Alembic commands ###
