# 🪨📄✂️ Rock, Paper, Scissors Game  
A simple and interactive **Rock, Paper, Scissors** game built with **HTML**, **CSS**, and **JavaScript**.  
The game allows the user to play against the computer, and the first to reach **three points** wins.

---

## 🎮 Features

### ✔️ Core Functionality
- Player chooses **Rock**, **Paper**, or **Scissors**
- Computer randomly generates one of the three options
- Round results are shown immediately
- Scores update in real-time
- The first to reach **3 points** wins the game

### ✔️ Game Logic
- Rock beats Scissors  
- Scissors beats Paper  
- Paper beats Rock  
- A tie occurs when both sides choose the same option

### ✔️ Additional Features
- A message is displayed showing the final winner
- Gameplay buttons are hidden when the game ends
- A **"Play Again?"** button resets everything

---

## 🧠 How It Works

### **1. Computer Choice**
```js
function getRandomComputerResult() {
  const options = ["Rock", "Paper", "Scissors"];
  const randomIndex = Math.floor(Math.random() * options.length);
  return options[randomIndex];
}

function hasPlayerWonTheRound(player, computer) {
  return (
    (player === "Rock" && computer === "Scissors") ||
    (player === "Scissors" && computer === "Paper") ||
    (player === "Paper" && computer === "Rock")
  );
}

/project-folder
│── index.html        # Game UI
│── styles.css        # Styling
│── script.js         # Game logic
│── README.md         # Documentation
