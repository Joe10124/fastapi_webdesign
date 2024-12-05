"""Initial migration

Revision ID: 8a08d4dc4492
Revises: 
Create Date: 2024-12-05 15:04:56.051685

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a08d4dc4492'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('completed', sa.Boolean(), nullable=True),
    sa.Column('sort', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_todos_description'), 'todos', ['description'], unique=False)
    op.create_index(op.f('ix_todos_id'), 'todos', ['id'], unique=False)
    op.create_index(op.f('ix_todos_title'), 'todos', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_todos_title'), table_name='todos')
    op.drop_index(op.f('ix_todos_id'), table_name='todos')
    op.drop_index(op.f('ix_todos_description'), table_name='todos')
    op.drop_table('todos')
    # ### end Alembic commands ###
