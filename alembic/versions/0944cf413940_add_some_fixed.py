"""Add some fixed

Revision ID: 0944cf413940
Revises: 36a9875ee4d0
Create Date: 2025-03-10 16:02:13.400981

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0944cf413940'
down_revision: Union[str, None] = '36a9875ee4d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subjects', sa.Column('department_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'subjects', 'departments', ['department_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subjects', type_='foreignkey')
    op.drop_column('subjects', 'department_id')
    # ### end Alembic commands ###
