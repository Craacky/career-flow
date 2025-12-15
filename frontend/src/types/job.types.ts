export interface Job {
  id: string;
  title: string;
  company: string;
  location: string;
  salaryMin: number;
  salaryMax: number;
  description: string;
  requirements: string[];
  responsibilities: string[];
  benefits: string[];
  postedDate: string;
  level: 'Junior' | 'Middle' | 'Senior' | 'Lead' | 'Executive';
  workFormat: 'Remote' | 'Office' | 'Hybrid' | 'Flexible';
  technologies: string[];
  experience: number;
  isSaved?: boolean;
  isApplied?: boolean;
}

export interface JobFilters {
  salaryRange?: [number, number];
  levels?: string[];
  technologies?: string[];
  workFormat?: string[];
  experience?: number;
}

export interface JobSearchParams {
  query?: string;
  filters?: JobFilters;
  page?: number;
  limit?: number;
}