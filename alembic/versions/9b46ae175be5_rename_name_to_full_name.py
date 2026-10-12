"""rename name to full name

Revision ID: 9b46ae175be5
Revises: d755a134d384
Create Date: 2026-10-07 19:20:45.031662

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b46ae175be5'
down_revision: Union[str, Sequence[str], None] = 'd755a134d384'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
