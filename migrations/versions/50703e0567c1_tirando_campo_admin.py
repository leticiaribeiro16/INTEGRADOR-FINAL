"""tirando campo admin

Revision ID: 50703e0567c1
Revises: 5bac55f5eaee
Create Date: 2023-01-18 17:53:40.491117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50703e0567c1'
down_revision = '5bac55f5eaee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.drop_column('admin')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('admin', sa.BOOLEAN(), nullable=True))

    # ### end Alembic commands ###
