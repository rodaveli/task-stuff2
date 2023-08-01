import React, { Component } from 'react';

class Streak extends Component {
    constructor(props) {
        super(props);
        this.state = {
            streak: 0
        };
    }

    componentDidMount() {
        this.updateStreak();
    }

    updateStreak() {
        // Fetch the updated streak from the server
        fetch('/api/streak')
            .then(response => response.json())
            .then(data => {
                this.setState({
                    streak: data.streak
                });
            });
    }

    render() {
        return (
            <div id="streak">
                <h2>Streak</h2>
                <p>{this.state.streak}</p>
            </div>
        );
    }
}

export default Streak;