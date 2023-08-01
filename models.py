```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    points = db.Column(db.Integer, default=0)
    streak = db.Column(db.Integer, default=0)

    def calculate_points(self):
        tasks = Task.query.filter_by(user_id=self.id, completed=True).all()
        self.points = sum(task.points for task in tasks)
        db.session.commit()

    def calculate_streak(self):
        today = datetime.today()
        tasks = Task.query.filter_by(user_id=self.id, completed=True).all()
        tasks.sort(key=lambda x: x.date)
        streak = 0
        for i in range(len(tasks) - 1, -1, -1):
            if (today - tasks[i].date).days > 1:
                break
            streak += 1
        self.streak = streak
        db.session.commit()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))
    points = db.Column(db.Integer, nullable=False)
    recurring_days = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def complete(self):
        self.completed = True
        db.session.commit()
```