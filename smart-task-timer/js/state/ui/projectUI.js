import { store } from "../state/store.js";

export function renderProjects() {
  const list = document.getElementById("projectList");
  list.innerHTML = "";

  store.projects.forEach(project => {
    const li = document.createElement("li");
    li.textContent = project.name;
    li.onclick = () => store.setActiveProject(project.id);
    list.appendChild(li);
  });
}
