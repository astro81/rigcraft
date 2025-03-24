import axios from "axios";

//! Fetch the url from the environment
const API_BASE_URL = import.meta.env.VITE_API_URL + '/api/component_category/';


export const component_category = async() => {
    const response = await axios.get(`${API_BASE_URL}`);
    return response.data;
}

