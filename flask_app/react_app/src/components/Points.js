import React, { Component } from 'react';
import { getPoints } from '../services/api';

class Points extends Component {
    constructor(props) {
        super(props);
        this.state = {
            points: 0
        };
    }

    componentDidMount() {
        getPoints()
            .then(response => {
                this.setState({
                    points: response.data.points
                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

    render() {
        return (
            <div id="points-display">
                <h2>Your Points</h2>
                <p>{this.state.points}</p>
            </div>
        );
    }
}

export default Points;