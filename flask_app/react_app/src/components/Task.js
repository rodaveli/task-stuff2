import React, { Component } from 'react';
import taskService from '../services/taskService';

class Task extends Component {
    constructor(props) {
        super(props);
        this.state = {
            id: this.props.id,
            name: this.props.name,
            points: this.props.points,
            recurrence: this.props.recurrence,
            completed: this.props.completed
        };
    }

    completeTask = () => {
        this.setState({ completed: true });
        taskService.update_task(this.state.id, { completed: true });
    }

    failTask = () => {
        this.setState({ completed: false });
        taskService.update_task(this.state.id, { completed: false });
    }

    render() {
        return (
            <div className="task-item">
                <h3>{this.state.name}</h3>
                <p>Points: {this.state.points}</p>
                <p>Recurrence: Every {this.state.recurrence} days</p>
                <button onClick={this.completeTask}>Complete Task</button>
                <button onClick={this.failTask}>Fail Task</button>
            </div>
        );
    }
}

export default Task;