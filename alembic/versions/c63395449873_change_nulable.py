"""Change nulable

Revision ID: c63395449873
Revises: f382193b863b
Create Date: 2025-02-07 15:56:17.221080

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c63395449873'
down_revision: Union[str, None] = 'f382193b863b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('students', 'last_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('students', 'first_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('students', 'patronymic',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('students', 'group_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('students', 'jshir',
               existing_type=sa.VARCHAR(length=15),
               nullable=True)
    op.alter_column('students', 'passport',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('students', 'passport',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('students', 'jshir',
               existing_type=sa.VARCHAR(length=15),
               nullable=False)
    op.alter_column('students', 'group_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('students', 'patronymic',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('students', 'first_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('students', 'last_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###
