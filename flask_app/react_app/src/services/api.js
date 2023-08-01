import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export function getTasks() {
    return axios.get(`${API_URL}/tasks`);
}

export function getUser() {
    return axios.get(`${API_URL}/user`);
}

export function getPoints() {
    return axios.get(`${API_URL}/points`);
}

export function getStreak() {
    return axios.get(`${API_URL}/streak`);
}