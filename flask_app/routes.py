```python
from flask import request, jsonify
from flask_app import app, db
from flask_app.models import User, Task

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(title=data['title'], points=data['points'], recurring_days=data['recurring_days'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'TASK_CREATED'})

@app.route('/api/tasks/<id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    task = Task.query.get(id)
    task.title = data['title']
    task.points = data['points']
    task.recurring_days = data['recurring_days']
    db.session.commit()
    return jsonify({'message': 'TASK_UPDATED'})

@app.route('/api/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'TASK_DELETED'})

@app.route('/api/user/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify({'message': 'USER_UPDATED'})

@app.route('/api/user/<id>/points', methods=['PUT'])
def update_points(id):
    data = request.get_json()
    user = User.query.get(id)
    user.points = data['points']
    db.session.commit()
    return jsonify({'message': 'USER_POINTS_UPDATED'})

@app.route('/api/user/<id>/streak', methods=['PUT'])
def update_streak(id):
    data = request.get_json()
    user = User.query.get(id)
    user.streak = data['streak']
    db.session.commit()
    return jsonify({'message': 'STREAK_UPDATED'})
```