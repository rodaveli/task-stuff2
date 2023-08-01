import React, { Component } from 'react';
import TaskGrid from './TaskGrid';
import UserProfile from './UserProfile';
import Streak from './Streak';
import PointTotal from './PointTotal';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tasks: [],
      user: {},
      streak: 0,
      pointTotal: 0
    };
  }

  componentDidMount() {
    // Fetch tasks, user, streak, and point total from the server
    // and update the state accordingly
  }

  render() {
    return (
      <div id="app">
        <UserProfile user={this.state.user} />
        <Streak streak={this.state.streak} />
        <PointTotal pointTotal={this.state.pointTotal} />
        <TaskGrid tasks={this.state.tasks} />
      </div>
    );
  }
}

export default App;