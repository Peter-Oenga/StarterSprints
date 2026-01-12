# PocketKanban 🗂️  
*A Single-File Node.js Kanban CLI Application*

---

## 📌 Overview

**PocketKanban** is a fully functional **Kanban task management system implemented entirely in a single JavaScript file**.  
It runs as an interactive **Command Line Interface (CLI)** application using Node.js and stores all data locally in a JSON file.

The project is intentionally designed to be:

- **Dependency-free** (uses only Node.js core modules)
- **Portable** (one `.js` file, one `.json` database)
- **Readable & educational** (clear architecture inside one file)
- **Production-safe** (atomic writes, activity logging, validation)

This repository demonstrates how a complete application can be built, structured, and reasoned about **without frameworks** while still maintaining clean separation of concerns.

---

## 🧠 What This Project Does

PocketKanban allows you to:

- Create and manage **multiple boards**
- Track tasks across **Backlog → To Do → Doing → Done**
- Assign **priority, tags, due dates**
- Move tasks between columns
- View **statistics and activity history**
- Persist everything locally
- Interact entirely via a **terminal prompt**

All of this is implemented in **one JavaScript file**.

---

## 📁 Repository Structure

```text
.
├── pocket-kanban.js        # The entire application (≈1000 lines)
├── pocketkanban.db.json    # Auto-generated local database (on first run)
└── README.md               # This documentation
