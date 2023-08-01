import axios from 'axios';

const STREAK_API_BASE_URL = "/api/streak";

class StreakService {

    getStreak(userId) {
        return axios.get(STREAK_API_BASE_URL + '/' + userId);
    }

    updateStreak(userId, streak) {
        return axios.put(STREAK_API_BASE_URL + '/' + userId, streak);
    }
}

export default new StreakService();