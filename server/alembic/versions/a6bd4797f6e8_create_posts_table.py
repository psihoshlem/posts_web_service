"""create posts table

Revision ID: a6bd4797f6e8
Revises: 
Create Date: 2023-09-04 13:49:26.307747

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a6bd4797f6e8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(45), nullable=False),
        sa.Column('text', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('NOW()')),
    )

def downgrade():
    op.drop_table('posts')
