import axios from 'axios';

//! Fetch the url from the environment
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
export const getProfile = async (token) => {
    const response = await axios.get(`${API_BASE_URL}/profile/`, {
        headers: { Authorization: `Bearer ${token}` },
    });
    return response.data;
};


//*Fetch profile update endpoint
export const updateProfile = async (token, profileData) => {
    const response = await axios.patch(`${API_BASE_URL}/profile/`, profileData, {
        headers: { Authorization: `Bearer ${token}` },
    });
    return response.data;
};


//*Logout endpoint
export const logout = async (refreshToken) => {
    const response = await axios.post(
        `${API_BASE_URL}/logout/`, 
        { refresh_token: refreshToken },
        { headers: { 'Content-Type': 'application/json' },
    });
    return response.data;
};


//*Delete account endpoint
export const deleteAccount = async (token, password) => {
    const response = await axios.post(
        `${API_BASE_URL}/delete-account/`,
        { password },
        { headers: { 
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }}
    );
    return response.data;
};