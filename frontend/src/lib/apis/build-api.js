// $lib/apis/build-api.js
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL + '/api';

export async function createBuild(buildData, access_token) {
    if (!access_token) {
        console.error('No authentication token found');
        throw new Error('Authentication token is missing');
    }

    try {
        const response = await axios.post(`${API_BASE_URL}/builds/`, buildData, {
            headers: {
                'Authorization': `Bearer ${access_token}`,
                'Content-Type': 'application/json'
            }
        });
        return response.data;
    } catch (error) {
        console.error('Full error response:', error.response);
        throw error;
    }
}

export async function fetchUserBuilds(build_Id, access_token) {
    if (!access_token) {
        console.error('No authentication token found');
        throw new Error('Authentication token is missing');
    }

    try {
        const response = await axios.get(`${API_BASE_URL}/builds/${build_Id}/`, {
            headers: {
                'Authorization': `Bearer ${access_token}`,
                'Content-Type': 'application/json'
            }
        });
        return response.data;
    } catch (error) {
        console.error('Full error response:', error.response);
        throw error;
    }
}

