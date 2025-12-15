import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';

const subscriptionAPI = {
  getPlans: async () => {
    // Implementation will go here
    return axios.get(`${API_BASE_URL}/subscription/plans`);
  },

  getUserSubscription: async (token: string) => {
    // Implementation will go here
    return axios.get(`${API_BASE_URL}/subscription`, {
      headers: { Authorization: `Bearer ${token}` }
    });
  },

  createSubscription: async (planId: string, token: string) => {
    // Implementation will go here
    return axios.post(`${API_BASE_URL}/subscription`, { planId }, {
      headers: { Authorization: `Bearer ${token}` }
    });
  },

  cancelSubscription: async (token: string) => {
    // Implementation will go here
    return axios.delete(`${API_BASE_URL}/subscription`, {
      headers: { Authorization: `Bearer ${token}` }
    });
  },

  renewSubscription: async (token: string) => {
    // Implementation will go here
    return axios.post(`${API_BASE_URL}/subscription/renew`, {}, {
      headers: { Authorization: `Bearer ${token}` }
    });
  }
};

export default subscriptionAPI;