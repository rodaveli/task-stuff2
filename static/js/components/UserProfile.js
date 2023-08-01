import React, { Component } from 'react';

class UserProfile extends Component {
  constructor(props) {
    super(props);
    this.state = {
      points: 0
    };
  }

  componentDidMount() {
    this.getUserPoints();
  }

  getUserPoints() {
    // Fetch user points from the server
    fetch('/api/user/points')
      .then(response => response.json())
      .then(data => {
        this.setState({ points: data.points });
      })
      .catch(error => console.error('Error:', error));
  }

  render() {
    return (
      <div id="user-profile">
        <h2>User Profile</h2>
        <p>Total Points: {this.state.points}</p>
      </div>
    );
  }
}

export default UserProfile;