import { create } from 'zustand';

interface AuthState {
  isAuthenticated: boolean;
  user: any | null;
  token: string | null;
  login: (token: string, userData: any) => void;
  logout: () => void;
  updateUser: (userData: any) => void;
}

const useAuthStore = create<AuthState>((set) => ({
  isAuthenticated: false,
  user: null,
  token: null,
  login: (token, userData) => set({ isAuthenticated: true, token, user: userData }),
  logout: () => set({ isAuthenticated: false, token: null, user: null }),
  updateUser: (userData) => set({ user: userData }),
}));

export default useAuthStore;