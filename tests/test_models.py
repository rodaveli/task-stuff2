```python
import unittest
from models import db, User, Task
from app import create_app

class TestModels(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_user(self):
        user = User(username='testuser', email='testuser@example.com')
        db.session.add(user)
        db.session.commit()
        self.assertEqual(User.query.count(), 1)

    def test_create_task(self):
        task = Task(title='Test Task', description='This is a test task', points=5, recurring_days=2)
        db.session.add(task)
        db.session.commit()
        self.assertEqual(Task.query.count(), 1)

    def test_calculate_streak(self):
        user = User(username='testuser', email='testuser@example.com')
        db.session.add(user)
        task1 = Task(title='Test Task 1', description='This is a test task', points=5, recurring_days=2, user_id=user.id)
        task2 = Task(title='Test Task 2', description='This is a test task', points=3, recurring_days=2, user_id=user.id)
        db.session.add(task1)
        db.session.add(task2)
        db.session.commit()
        user.calculate_streak()
        self.assertEqual(user.streak, 1)

    def test_calculate_points(self):
        user = User(username='testuser', email='testuser@example.com')
        db.session.add(user)
        task1 = Task(title='Test Task 1', description='This is a test task', points=5, recurring_days=2, user_id=user.id)
        task2 = Task(title='Test Task 2', description='This is a test task', points=3, recurring_days=2, user_id=user.id)
        db.session.add(task1)
        db.session.add(task2)
        db.session.commit()
        user.calculate_points()
        self.assertEqual(user.points, 8)

if __name__ == '__main__':
    unittest.main()
```