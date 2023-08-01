import React, { Component } from 'react';

class PointTotal extends Component {
    constructor(props) {
        super(props);
        this.state = {
            points: 0
        };
    }

    componentDidMount() {
        this.getPoints();
    }

    getPoints() {
        fetch('/api/user/points')
            .then(response => response.json())
            .then(data => this.setState({ points: data.points }));
    }

    render() {
        return (
            <div id="point-total">
                <h2>Point Total</h2>
                <p>{this.state.points}</p>
            </div>
        );
    }
}

export default PointTotal;