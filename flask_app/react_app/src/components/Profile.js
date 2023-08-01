import React, { Component } from 'react';
import { getUser, getPoints } from '../services/userService';

class Profile extends Component {
  constructor(props) {
    super(props);
    this.state = {
      user: {},
      points: 0
    };
  }

  componentDidMount() {
    this.loadUserProfile();
  }

  loadUserProfile = async () => {
    const user = await getUser();
    const points = await getPoints();
    this.setState({ user, points });
  }

  render() {
    const { user, points } = this.state;
    return (
      <div id="user-profile">
        <h2>{user.name}'s Profile</h2>
        <p>Total Points: {points}</p>
      </div>
    );
  }
}

export default Profile;