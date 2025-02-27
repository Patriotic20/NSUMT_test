"""Add user table

Revision ID: 5582ba5cb909
Revises: 30336cc27d6f
Create Date: 2025-02-06 20:34:07.962853

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5582ba5cb909'
down_revision: Union[str, None] = '30336cc27d6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('role', sa.Enum('student', 'teacher', 'admin', name='userrole'), nullable=True),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.add_column('students', sa.Column('user_id', sa.Integer(), nullable=True))
    op.alter_column('students', 'jshir',
               existing_type=sa.VARCHAR(length=14),
               type_=sa.String(length=15),
               existing_nullable=False)
    op.create_foreign_key(None, 'students', 'users', ['user_id'], ['id'])
    op.add_column('teachers', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'teachers', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'teachers', type_='foreignkey')
    op.drop_column('teachers', 'user_id')
    op.drop_constraint(None, 'students', type_='foreignkey')
    op.alter_column('students', 'jshir',
               existing_type=sa.String(length=15),
               type_=sa.VARCHAR(length=14),
               existing_nullable=False)
    op.drop_column('students', 'user_id')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
