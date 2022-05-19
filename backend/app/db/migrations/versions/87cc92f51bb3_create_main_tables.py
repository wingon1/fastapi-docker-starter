"""create_main_tables

Revision ID: 87cc92f51bb3
Revises: 
Create Date: 2022-05-19 02:53:18.793681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '87cc92f51bb3'
down_revision = None
branch_labels = None
depends_on = None


def create_users_table() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
    )

def upgrade() -> None:
    create_users_table()


def downgrade() -> None:
    op.drop_table("users")