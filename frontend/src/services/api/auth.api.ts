import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';

const authAPI = {
  login: async (email: string, password: string) => {
    // Implementation will go here
    return axios.post(`${API_BASE_URL}/auth/login`, { email, password });
  },

  register: async (userData: any) => {
    // Implementation will go here
    return axios.post(`${API_BASE_URL}/auth/register`, userData);
  },

  logout: async () => {
    // Implementation will go here
    return axios.post(`${API_BASE_URL}/auth/logout`);
  },

  getCurrentUser: async (token: string) => {
    // Implementation will go here
    return axios.get(`${API_BASE_URL}/auth/me`, {
      headers: { Authorization: `Bearer ${token}` }
    });
  },

  refreshToken: async (refreshToken: string) => {
    // Implementation will go here
    return axios.post(`${API_BASE_URL}/auth/refresh`, { refreshToken });
  }
};

export default authAPI;