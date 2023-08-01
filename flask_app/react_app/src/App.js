import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Grid from './components/Grid';
import Profile from './components/Profile';
import Task from './components/Task';
import Streak from './components/Streak';
import Points from './components/Points';

import { getTasks, getUser, getPoints, getStreak } from './services/api';

class App extends Component {
  state = {
    tasks: [],
    user: {},
    points: 0,
    streak: 0
  };

  componentDidMount() {
    this.loadTasks();
    this.loadUser();
    this.loadPoints();
    this.loadStreak();
  }

  loadTasks = async () => {
    const tasks = await getTasks();
    this.setState({ tasks });
  };

  loadUser = async () => {
    const user = await getUser();
    this.setState({ user });
  };

  loadPoints = async () => {
    const points = await getPoints();
    this.setState({ points });
  };

  loadStreak = async () => {
    const streak = await getStreak();
    this.setState({ streak });
  };

  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/" component={Grid} />
          <Route path="/profile" component={Profile} />
          <Route path="/task/:id" component={Task} />
          <Route path="/streak" component={Streak} />
          <Route path="/points" component={Points} />
        </Switch>
      </Router>
    );
  }
}

export default App;