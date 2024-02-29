"""empty message

Revision ID: 356ac2a897cc
Revises: 
Create Date: 2024-02-25 19:55:58.092580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '356ac2a897cc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('folk',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('working_title', sa.String(length=150), nullable=True),
    sa.Column('genre', sa.String(length=50), nullable=True),
    sa.Column('writer_name', sa.String(length=100), nullable=True),
    sa.Column('length', sa.String(length=15), nullable=True),
    sa.Column('rating', sa.String(length=25), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rhythm',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('working_title', sa.String(length=150), nullable=True),
    sa.Column('genre', sa.String(length=50), nullable=True),
    sa.Column('writer_name', sa.String(length=100), nullable=True),
    sa.Column('length', sa.String(length=15), nullable=True),
    sa.Column('rating', sa.String(length=25), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rock',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('working_title', sa.String(length=150), nullable=True),
    sa.Column('genre', sa.String(length=50), nullable=True),
    sa.Column('writer_name', sa.String(length=100), nullable=True),
    sa.Column('length', sa.String(length=15), nullable=True),
    sa.Column('rating', sa.String(length=25), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rock')
    op.drop_table('rhythm')
    op.drop_table('folk')
    op.drop_table('user')
    # ### end Alembic commands ###