import { projectService } from "./services/projectService.js";
import { taskService } from "./services/taskService.js";
import { store } from "./state/store.js";
import { renderProjects } from "./ui/projectUI.js";
import { renderDashboard } from "./ui/dashboardUI.js";

projectService.init();

store.subscribe(() => {
  renderProjects();
  renderDashboard();
});

document.getElementById("newProjectBtn").onclick = () => {
  const name = prompt("Project name:");
  if (name) projectService.createProject(name);
};

document.getElementById("addTaskBtn").onclick = () => {
  taskService.addTask({
    name: document.getElementById("taskName").value,
    priority: document.getElementById("taskPriority").value,
    deadline: document.getElementById("taskDeadline").value
  });
};
