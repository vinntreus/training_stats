"""Add workouts table

Revision ID: 9cd42e48cd23
Revises:
Create Date: 2017-02-26 15:19:51.725179

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9cd42e48cd23'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('workouts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('date', sa.DATE(), nullable=False),
        sa.Column('exercises', postgresql.JSON(astext_type=sa.Text()), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('workouts')
