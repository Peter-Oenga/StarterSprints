# 🎮 React Tic-Tac-Toe Game

This project is a complete **Tic-Tac-Toe game built with React**, closely following the logic and structure presented in the official React documentation tutorial. It demonstrates key React concepts such as component composition, state management, event handling, and implementing time travel through state history.

---

## 🚀 Features

- **Interactive Tic-Tac-Toe gameplay**
- **X/O turn switching**
- **Winner detection**
- **Move history tracking ("time travel")**
- **Ability to jump back to any previous move**
- **Simple and clean React architecture**

---

## 🧠 Key React Concepts Used

### ✔ Functional Components  
Components (`Square`, `Board`, `Game`) are implemented using modern React function components.

### ✔ State Management with `useState`  
- Board history is stored in an array of moves  
- Current move index determines whose turn it is  
- Full time-travel capability is implemented by slicing history  

### ✔ Component Composition  
Game → Board → Square  
Each part manages exactly what it needs, following React's recommended design.

### ✔ Event Handling  
Clicking a square triggers `onSquareClick`, updating board state and progressing gameplay.

### ✔ Pure Functions  
The `calculateWinner` function evaluates winning positions without mutating state.

---

## 📂 Project Structure (Core Logic Only)





(Your code may be structured in a single file — this is just a recommended modular layout.)

---

## 📜 Code Overview

### 🔸 Square Component
Renders a single square button and triggers its click handler.

### 🔸 Board Component
- Renders the 3x3 grid
- Handles user moves  
- Prevents overwriting existing moves  
- Displays game status (winner or next player)

### 🔸 Game Component
- Stores full move history  
- Handles time travel  
- Passes state down to the Board  
- Renders the list of moves  

### 🔸 calculateWinner Function
Evaluates all winning combinations and returns the winner if one exists.

---

## ▶️ How to Run This Project

### **1. Install dependencies**
```sh
npm install
