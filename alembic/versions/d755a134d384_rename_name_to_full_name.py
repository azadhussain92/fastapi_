"""rename name to full_name

Revision ID: d755a134d384
Revises: e9673e8d55f2
Create Date: 2026-10-06 13:14:44.207610

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd755a134d384'
down_revision: Union[str, Sequence[str], None] = 'e9673e8d55f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column('name',new_column_name='full_name')


def downgrade() -> None:
    """Downgrade schema."""
    pass

