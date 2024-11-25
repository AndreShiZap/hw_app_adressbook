"""Add table user

Revision ID: 88080dbcd2af
Revises: 145c35e5afe4
Create Date: 2024-11-14 12:08:14.132138

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88080dbcd2af'
down_revision: Union[str, None] = '145c35e5afe4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('avatar', sa.String(length=255), nullable=True),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.add_column('contact', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('contact', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('contact', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'contact', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contact', type_='foreignkey')
    op.drop_column('contact', 'user_id')
    op.drop_column('contact', 'updated_at')
    op.drop_column('contact', 'created_at')
    op.drop_table('users')
    # ### end Alembic commands ###
