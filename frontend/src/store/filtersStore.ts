import { create } from 'zustand';

interface FiltersState {
  salaryRange: [number, number];
  jobLevel: string[];
  technologies: string[];
  workFormat: string[];
  experience: string;
  resetFilters: () => void;
  updateSalaryRange: (range: [number, number]) => void;
  updateJobLevel: (levels: string[]) => void;
  updateTechnologies: (tech: string[]) => void;
  updateWorkFormat: (format: string[]) => void;
  updateExperience: (exp: string) => void;
}

const useFiltersStore = create<FiltersState>((set) => ({
  salaryRange: [0, 500000],
  jobLevel: [],
  technologies: [],
  workFormat: [],
  experience: '',
  resetFilters: () => set({
    salaryRange: [0, 500000],
    jobLevel: [],
    technologies: [],
    workFormat: [],
    experience: '',
  }),
  updateSalaryRange: (range) => set({ salaryRange: range }),
  updateJobLevel: (levels) => set({ jobLevel: levels }),
  updateTechnologies: (tech) => set({ technologies: tech }),
  updateWorkFormat: (format) => set({ workFormat: format }),
  updateExperience: (exp) => set({ experience: exp }),
}));

export default useFiltersStore;