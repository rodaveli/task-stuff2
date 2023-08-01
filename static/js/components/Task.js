import React from 'react';

class Task extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            id: props.id,
            name: props.name,
            points: props.points,
            recurrence: props.recurrence,
            completed: props.completed
        };
    }

    handleComplete() {
        this.setState({completed: true});
        // TODO: Send a request to the server to update the task status
    }

    render() {
        return (
            <div id={`task-${this.state.id}`} className="task">
                <h3>{this.state.name}</h3>
                <p>Points: {this.state.points}</p>
                <p>Recurs every {this.state.recurrence} days</p>
                <button onClick={this.handleComplete.bind(this)}>
                    {this.state.completed ? 'Completed' : 'Mark as Complete'}
                </button>
            </div>
        );
    }
}

export default Task;