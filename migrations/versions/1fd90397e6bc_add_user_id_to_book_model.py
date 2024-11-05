"""Add user_id to Book model

Revision ID: 1fd90397e6bc
Revises: 
Create Date: 2024-11-05 10:33:33.704801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fd90397e6bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_book_user_id', 'user', ['user_id'], ['id'])

def downgrade():
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_constraint('fk_book_user_id', type_='foreignkey')
        batch_op.drop_column('user_id')