"""rename department

Revision ID: 0123e106cfd2
Revises: b673ec0aafca
Create Date: 2024-02-21 10:10:11.139911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0123e106cfd2'
down_revision = 'b673ec0aafca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###