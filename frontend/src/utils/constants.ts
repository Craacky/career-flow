// API Endpoints
export const API_ENDPOINTS = {
  AUTH: {
    LOGIN: '/auth/login',
    REGISTER: '/auth/register',
    LOGOUT: '/auth/logout',
    REFRESH: '/auth/refresh',
    ME: '/auth/me',
  },
  JOBS: {
    ALL: '/jobs',
    BY_ID: (id: string) => `/jobs/${id}`,
    SEARCH: '/jobs/search',
    APPLY: (id: string) => `/jobs/${id}/apply`,
    SAVE: (id: string) => `/jobs/${id}/save`,
  },
  USER: {
    PROFILE: '/user/profile',
    PASSWORD: '/user/password',
    SAVED_JOBS: '/user/saved-jobs',
    APPLICATIONS: '/user/applications',
  },
  SUBSCRIPTION: {
    PLANS: '/subscription/plans',
    MAIN: '/subscription',
    RENEW: '/subscription/renew',
  },
};

// Job constants
export const JOB_LEVELS = ['Junior', 'Middle', 'Senior', 'Lead', 'Executive'];
export const WORK_FORMATS = ['Remote', 'Office', 'Hybrid', 'Flexible'];
export const SALARY_PERIODS = ['year', 'month', 'hour'];

// UI constants
export const THEMES = ['light', 'dark'];
export const ROUTES = {
  HOME: '/',
  JOBS: '/jobs',
  JOB_DETAILS: (id: string) => `/jobs/${id}`,
  LOGIN: '/login',
  REGISTER: '/register',
  PROFILE: '/profile',
  SUBSCRIPTION: '/subscription',
  ADMIN: '/admin',
  NOT_FOUND: '/404',
};

// Application constants
export const APP_NAME = 'CareerFlow';
export const COMPANY_NAME = 'CareerFlow Inc.';
export const SUPPORT_EMAIL = 'support@careerflow.com';
export const VERSION = '1.0.0';