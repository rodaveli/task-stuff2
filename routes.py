
from flask import Flask, request, jsonify
from models import db, Task, User
from app import app

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(data['title'], data['points'], data['recurrence'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'TASK_CREATED', 'task': new_task.serialize()}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    task.title = data['title']
    task.points = data['points']
    task.recurrence = data['recurrence']
    db.session.commit()
    return jsonify({'message': 'TASK_UPDATED', 'task': task.serialize()}), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'TASK_DELETED'}), 200

@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user.streak = data['streak']
    user.points = data['points']
    db.session.commit()
    return jsonify({'message': 'USER_UPDATED', 'user': user.serialize()}), 200
