import { storageService } from "./storageService.js";
import { store } from "../state/store.js";
import { uuid } from "../utils/uuid.js";

export const projectService = {
  init() {
    store.setProjects(storageService.load());
  },

  createProject(name) {
    const project = {
      id: uuid(),
      name,
      createdAt: Date.now(),
      tasks: []
    };

    store.projects.push(project);
    storageService.save(store.projects);
    store.setActiveProject(project.id);
  },

  deleteProject(id) {
    store.setProjects(store.projects.filter(p => p.id !== id));
    storageService.save(store.projects);
  }
};
