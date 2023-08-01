import axios from 'axios';

const POINTS_API_BASE_URL = "/api/points";

class PointService {

    getPoints(userId) {
        return axios.get(POINTS_API_BASE_URL + '/' + userId);
    }

    updatePoints(userId, points) {
        return axios.put(POINTS_API_BASE_URL + '/' + userId, points);
    }

    deductPoints(userId, penalty) {
        return axios.put(POINTS_API_BASE_URL + '/deduct/' + userId, penalty);
    }
}

export default new PointService();