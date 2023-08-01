import React, { Component } from 'react';
import Task from './Task';

class TaskGrid extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tasks: []
    };
  }

  componentDidMount() {
    fetch('/api/tasks')
      .then(response => response.json())
      .then(data => this.setState({ tasks: data }));
  }

  renderTasks() {
    return this.state.tasks.map(task => (
      <Task key={task.id} task={task} />
    ));
  }

  render() {
    return (
      <div id="task-grid">
        {this.renderTasks()}
      </div>
    );
  }
}

export default TaskGrid;