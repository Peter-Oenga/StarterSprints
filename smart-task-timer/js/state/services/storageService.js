const KEY = "projectops-data";

export const storageService = {
  load() {
    try {
      return JSON.parse(localStorage.getItem(KEY)) || [];
    } catch {
      return [];
    }
  },

  save(data) {
    localStorage.setItem(KEY, JSON.stringify(data));
  }
};
