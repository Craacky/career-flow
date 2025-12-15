export interface User {
  id: string;
  email: string;
  firstName: string;
  lastName: string;
  avatar?: string;
  role: 'job_seeker' | 'employer' | 'admin';
  subscription?: Subscription;
  createdAt: string;
  updatedAt: string;
}

export interface UserProfile {
  id: string;
  firstName: string;
  lastName: string;
  email: string;
  phone?: string;
  location?: string;
  bio?: string;
  avatar?: string;
  resumeUrl?: string;
  experience?: number;
  skills?: string[];
  jobPreferences?: JobPreferences;
  socialLinks?: SocialLinks;
}

export interface JobPreferences {
  preferredLocations: string[];
  preferredJobTypes: string[];
  salaryExpectation: number;
  noticePeriod: number;
  remoteWork: boolean;
}

export interface SocialLinks {
  linkedin?: string;
  github?: string;
  portfolio?: string;
  twitter?: string;
}

export interface Subscription {
  id: string;
  planId: string;
  name: string;
  features: string[];
  price: number;
  status: 'active' | 'inactive' | 'expired';
  startDate: string;
  endDate: string;
}