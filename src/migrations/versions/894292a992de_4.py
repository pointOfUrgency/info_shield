"""4

Revision ID: 894292a992de
Revises: dd4940497c24
Create Date: 2024-02-10 22:09:44.895286

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '894292a992de'
down_revision: Union[str, None] = 'dd4940497c24'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('date_time', sa.TIMESTAMP(), nullable=True))
    op.add_column('content', sa.Column('date_time', sa.TIMESTAMP(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('content', 'date_time')
    op.drop_column('comment', 'date_time')
    # ### end Alembic commands ###
