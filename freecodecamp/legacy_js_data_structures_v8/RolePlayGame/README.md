# 🐉 Dragon Repeller – Simple RPG Game

Dragon Repeller is a small browser-based RPG game built with **HTML, CSS, and JavaScript**.  
The player navigates between locations, manages health and gold, and prepares to fight monsters and a dragon.

---

## 🎮 Features

- Location-based navigation (Town Square, Store, Cave)
- Player stats: **XP, Health, Gold**
- Interactive buttons to move and perform actions
- Dynamic text updates based on player actions
- Basic UI styled with CSS

---

## 🗂 Project Structure


---

## ⚙️ How the Game Works

### Game State Variables

These variables track the player’s progress:

```js
let xp = 0;
let health = 100;
let gold = 50;
let currentWeaponIndex = 0;
let inventory = ["stick"];
