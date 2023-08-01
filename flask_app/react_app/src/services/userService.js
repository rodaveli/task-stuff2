import axios from 'axios';

const USER_API_BASE_URL = "/api/users";

class UserService {

    getUser(userId) {
        return axios.get(USER_API_BASE_URL + '/' + userId);
    }

    updateUser(userId, user) {
        return axios.put(USER_API_BASE_URL + '/' + userId, user);
    }

    updatePoints(userId, points) {
        return axios.put(USER_API_BASE_URL + '/' + userId + '/points', { points: points });
    }
}

export default new UserService();