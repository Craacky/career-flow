import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';

const userAPI = {
  getProfile: async (token: string) => {
    // Implementation will go here
    return axios.get(`${API_BASE_URL}/user/profile`, {
      headers: { Authorization: `Bearer ${token}` }
    });
  },

  updateProfile: async (profileData: any, token: string) => {
    // Implementation will go here
    return axios.put(`${API_BASE_URL}/user/profile`, profileData, {
      headers: { Authorization: `Bearer ${token}` }
    });
  },

  updatePassword: async (passwordData: any, token: string) => {
    // Implementation will go here
    return axios.put(`${API_BASE_URL}/user/password`, passwordData, {
      headers: { Authorization: `Bearer ${token}` }
    });
  },

  getSavedJobs: async (token: string) => {
    // Implementation will go here
    return axios.get(`${API_BASE_URL}/user/saved-jobs`, {
      headers: { Authorization: `Bearer ${token}` }
    });
  },

  getApplications: async (token: string) => {
    // Implementation will go here
    return axios.get(`${API_BASE_URL}/user/applications`, {
      headers: { Authorization: `Bearer ${token}` }
    });
  }
};

export default userAPI;