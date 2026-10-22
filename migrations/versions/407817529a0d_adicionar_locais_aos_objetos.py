
"""Adicionar locais aos objetos

Revision ID: 407817529a0d
Revises: 2a75429d9bf1
Create Date: 2026-10-21 20:52:01.806459
"""

from alembic import op
import sqlalchemy as sa


revision = '407817529a0d'
down_revision = '2a75429d9bf1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'local',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('nome')
    )

    with op.batch_alter_table('objeto', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('local_id', sa.Integer(), nullable=False)
        )
        batch_op.add_column(
            sa.Column('detalhes_local', sa.String(length=100), nullable=False)
        )
        batch_op.create_foreign_key(
            'fk_objeto_local_id_local',
            'local',
            ['local_id'],
            ['id']
        )
        batch_op.drop_column('local')


def downgrade():
    with op.batch_alter_table('objeto', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('local', sa.String(length=100), nullable=False)
        )
        batch_op.drop_constraint(
            'fk_objeto_local_id_local',
            type_='foreignkey'
        )
        batch_op.drop_column('detalhes_local')
        batch_op.drop_column('local_id')

    op.drop_table('local')
