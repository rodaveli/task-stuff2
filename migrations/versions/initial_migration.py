```python
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM

def upgrade():
    # create enum type for task points
    task_points = ENUM('1', '3', '5', name='task_points', create_type=False)
    task_points.create(op.get_bind())

    # create tasks table
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('description', sa.String(200), nullable=False),
        sa.Column('recurrence_days', sa.Integer, nullable=False),
        sa.Column('points', task_points, nullable=False),
        sa.Column('penalty', sa.Boolean, default=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'))
    )

    # create users table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False, unique=True),
        sa.Column('total_points', sa.Integer, default=0),
        sa.Column('streak', sa.Integer, default=0)
    )

def downgrade():
    op.drop_table('tasks')
    op.drop_table('users')
    ENUM(name='task_points').drop(op.get_bind())
```