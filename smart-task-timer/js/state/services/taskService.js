import { uuid } from "../utils/uuid.js";
import { store } from "../state/store.js";
import { storageService } from "./storageService.js";

export const taskService = {
  addTask(data) {
    const task = {
      id: uuid(),
      name: data.name,
      priority: data.priority,
      deadline: data.deadline,
      status: "todo",
      createdAt: Date.now()
    };

    store.activeProject.tasks.push(task);
    storageService.save(store.projects);
    store.notify();
  },

  updateStatus(taskId, status) {
    const task = store.activeProject.tasks.find(t => t.id === taskId);
    if (task) task.status = status;
    storageService.save(store.projects);
    store.notify();
  }
};
