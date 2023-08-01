```python
import unittest
from flask import Flask
from app import app
from models import db, User, Task

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/test_db'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        response = self.client.post('/task', data=dict(
            title="Test Task",
            description="This is a test task",
            points=3,
            recurring_days=2
        ))
        self.assertEqual(response.status_code, 201)
        task = Task.query.filter_by(title="Test Task").first()
        self.assertIsNotNone(task)

    def test_update_task(self):
        task = Task(title="Test Task", description="This is a test task", points=3, recurring_days=2)
        db.session.add(task)
        db.session.commit()
        response = self.client.put(f'/task/{task.id}', data=dict(
            title="Updated Test Task",
            description="This is an updated test task",
            points=5,
            recurring_days=3
        ))
        self.assertEqual(response.status_code, 200)
        updated_task = Task.query.get(task.id)
        self.assertEqual(updated_task.title, "Updated Test Task")

    def test_delete_task(self):
        task = Task(title="Test Task", description="This is a test task", points=3, recurring_days=2)
        db.session.add(task)
        db.session.commit()
        response = self.client.delete(f'/task/{task.id}')
        self.assertEqual(response.status_code, 200)
        deleted_task = Task.query.get(task.id)
        self.assertIsNone(deleted_task)

if __name__ == "__main__":
    unittest.main()
```