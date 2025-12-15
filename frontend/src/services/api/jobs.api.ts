import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';

const jobsAPI = {
  getAllJobs: async (params?: any) => {
    // Implementation will go here
    return axios.get(`${API_BASE_URL}/jobs`, { params });
  },

  getJobById: async (id: string) => {
    // Implementation will go here
    return axios.get(`${API_BASE_URL}/jobs/${id}`);
  },

  searchJobs: async (query: string, filters?: any) => {
    // Implementation will go here
    return axios.get(`${API_BASE_URL}/jobs/search`, { 
      params: { query, ...filters } 
    });
  },

  applyForJob: async (jobId: string, applicationData: any, token: string) => {
    // Implementation will go here
    return axios.post(`${API_BASE_URL}/jobs/${jobId}/apply`, applicationData, {
      headers: { Authorization: `Bearer ${token}` }
    });
  },

  saveJob: async (jobId: string, token: string) => {
    // Implementation will go here
    return axios.post(`${API_BASE_URL}/jobs/${jobId}/save`, {}, {
      headers: { Authorization: `Bearer ${token}` }
    });
  }
};

export default jobsAPI;