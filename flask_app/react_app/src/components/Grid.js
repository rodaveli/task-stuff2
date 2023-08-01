import React, { Component } from 'react';
import Task from './Task';
import { getTasks } from '../services/api';

class Grid extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tasks: []
    };
  }

  componentDidMount() {
    getTasks().then(tasks => {
      this.setState({ tasks });
    });
  }

  render() {
    return (
      <div id="task-grid">
        {this.state.tasks.map(task => (
          <Task key={task.id} task={task} />
        ))}
      </div>
    );
  }
}

export default Grid;