```python
import unittest
from flask import json
from app import app
from models import db, Task, User

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db

    def test_create_task(self):
        response = self.app.post('/tasks', data=json.dumps({
            'title': 'Test Task',
            'points': 3,
            'recurring_days': 2
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'TASK_CREATED')

    def test_update_task(self):
        task = Task(title='Test Task', points=3, recurring_days=2)
        self.db.session.add(task)
        self.db.session.commit()
        response = self.app.put(f'/tasks/{task.id}', data=json.dumps({
            'title': 'Updated Task',
            'points': 5,
            'recurring_days': 3
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'TASK_UPDATED')

    def test_delete_task(self):
        task = Task(title='Test Task', points=3, recurring_days=2)
        self.db.session.add(task)
        self.db.session.commit()
        response = self.app.delete(f'/tasks/{task.id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'TASK_DELETED')

    def test_update_user(self):
        user = User(name='Test User', email='test@test.com', password='test')
        self.db.session.add(user)
        self.db.session.commit()
        response = self.app.put(f'/users/{user.id}', data=json.dumps({
            'name': 'Updated User',
            'email': 'updated@test.com',
            'password': 'updated'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'USER_UPDATED')

if __name__ == '__main__':
    unittest.main()
```