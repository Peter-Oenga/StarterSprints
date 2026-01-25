import { store } from "../state/store.js";

export function renderDashboard() {
  const el = document.getElementById("dashboard");

  let totalTasks = 0;
  let completed = 0;

  store.projects.forEach(p => {
    totalTasks += p.tasks.length;
    completed += p.tasks.filter(t => t.status === "done").length;
  });

  el.innerHTML = `
    <h2>Overview</h2>
    <p>Total Projects: ${store.projects.length}</p>
    <p>Total Tasks: ${totalTasks}</p>
    <p>Completed Tasks: ${completed}</p>
  `;
}
