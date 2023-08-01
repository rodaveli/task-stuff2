import React, { Component } from 'react';
import { getStreak } from '../services/streakService';

class Streak extends Component {
    state = {
        streak: 0
    };

    async componentDidMount() {
        const { data: streak } = await getStreak();
        this.setState({ streak });
    }

    render() {
        return (
            <div id="streak-display">
                <h2>Streak</h2>
                <p>{this.state.streak}</p>
            </div>
        );
    }
}

export default Streak;