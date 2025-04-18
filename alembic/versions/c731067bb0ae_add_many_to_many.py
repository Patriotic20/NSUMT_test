"""Add many-to-many

Revision ID: c731067bb0ae
Revises: 0219e83d2eb9
Create Date: 2025-02-13 15:06:30.773665

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c731067bb0ae'
down_revision: Union[str, None] = '0219e83d2eb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teacher_group_association',
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('teacher_id', 'group_id')
    )
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('imgae', sa.String(), nullable=True),
    sa.Column('A', sa.String(), nullable=False),
    sa.Column('B', sa.String(), nullable=False),
    sa.Column('C', sa.String(), nullable=False),
    sa.Column('D', sa.String(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_tests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('groups', sa.Column('department_id', sa.Integer(), nullable=False))
    op.drop_constraint('groups_teacher_id_fkey', 'groups', type_='foreignkey')
    op.create_foreign_key(None, 'groups', 'departments', ['department_id'], ['id'])
    op.drop_column('groups', 'teacher_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('groups', sa.Column('teacher_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'groups', type_='foreignkey')
    op.create_foreign_key('groups_teacher_id_fkey', 'groups', 'teachers', ['teacher_id'], ['id'])
    op.drop_column('groups', 'department_id')
    op.drop_table('user_tests')
    op.drop_table('questions')
    op.drop_table('teacher_group_association')
    # ### end Alembic commands ###
