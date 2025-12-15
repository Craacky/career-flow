import { create } from 'zustand';

interface UIState {
  isSidebarOpen: boolean;
  isModalOpen: boolean;
  modalContent: string | null;
  theme: 'light' | 'dark';
  toggleSidebar: () => void;
  openModal: (content: string) => void;
  closeModal: () => void;
  setTheme: (theme: 'light' | 'dark') => void;
  setIsModalOpen: (isOpen: boolean) => void;
}

const useUIStore = create<UIState>((set) => ({
  isSidebarOpen: false,
  isModalOpen: false,
  modalContent: null,
  theme: 'light',
  toggleSidebar: () => set((state) => ({ isSidebarOpen: !state.isSidebarOpen })),
  openModal: (content) => set({ isModalOpen: true, modalContent: content }),
  closeModal: () => set({ isModalOpen: false, modalContent: null }),
  setTheme: (theme) => set({ theme }),
  setIsModalOpen: (isOpen) => set({ isModalOpen: isOpen }),
}));

export default useUIStore;