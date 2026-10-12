"""add age column to users

Revision ID: e9673e8d55f2
Revises: 
Create Date: 2026-10-05 13:35:59.086004

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9673e8d55f2'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# def upgrade() -> None:
#     """Upgrade schema."""
#     op.add_column('users',sa.Column('age',op.Integer(),nullable=True))
def upgrade() -> None:
    op.add_column(
        'users',
        sa.Column('age', sa.Integer(), nullable=True)
    ) 


def downgrade() -> None:
    """Downgrade schema."""
    pass


# with op.batch_alter_table('users') as batch_op:
#     batch_op.alter_column('name',new_column_name='full_name')

# delete coloum
# op.drop_column('users','email') upgrade only
# op.add_column('user',sa.Column('email',sa.String(120),nullable=True)) downgrade 
