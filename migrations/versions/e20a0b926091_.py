"""Add foreign key to user in workouts table

Revision ID: e20a0b926091
Revises: 4b806c48d18d
Create Date: 2017-03-12 13:38:41.999381

"""
from alembic import op
import sqlalchemy as sa


revision = 'e20a0b926091'
down_revision = '4b806c48d18d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('workouts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'workouts', 'users', ['user_id'], ['id'])


def downgrade():
    op.drop_constraint(None, 'workouts', type_='foreignkey')
    op.drop_column('workouts', 'user_id')
