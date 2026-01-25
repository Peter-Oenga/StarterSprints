export const store = {
  projects: [],
  activeProjectId: null,
  listeners: [],

  subscribe(fn) {
    this.listeners.push(fn);
  },

  notify() {
    this.listeners.forEach(fn => fn(this));
  },

  setProjects(projects) {
    this.projects = projects;
    this.notify();
  },

  setActiveProject(id) {
    this.activeProjectId = id;
    this.notify();
  },

  get activeProject() {
    return this.projects.find(p => p.id === this.activeProjectId);
  }
};
