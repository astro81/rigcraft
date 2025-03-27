// user-api.js
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL + '/users';

//* Login endpoint
export const login = async (username, password) => {
    const response = await axios.post(`${API_BASE_URL}/login/`, { username, password });
    return response.data;
};


//* Register endpoint
export const register = async (userData) => {
    const response = await axios.post(`${API_BASE_URL}/register/`, userData);
    return response.data;
};


//*Fetch user profile endpoint
export const getProfile = async (access_token) => {
    const response = await axios.get(`${API_BASE_URL}/profile/`, {
        headers: { Authorization: `Bearer ${access_token}` },
    });
    return response.data;
};


//*Fetch profile update endpoint
export const updateProfile = async (access_token, profileData) => {
    const response = await axios.patch(`${API_BASE_URL}/profile/`, profileData, {
        headers: { Authorization: `Bearer ${access_token}` },
    });
    return response.data;
};


//*Logout endpoint
export const logout = async (access_token, refresh_token) => {
    const response = await axios.post(
        `${API_BASE_URL}/logout/`, 
        { refresh_token: refresh_token },
        { headers: { 
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${access_token}`
        }}
    );
    return response.data;
};


//*Delete account endpoint
export const deleteAccount = async (access_token, password) => {
    const response = await axios.post(
        `${API_BASE_URL}/delete-account/`,
        { password },
        { headers: { 
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${access_token}`
        }}
    );
    return response.data;
};


