# Football Team Cards – Modern JavaScript Practice

This project is a **dynamic football team cards application** built with **vanilla JavaScript, HTML, and CSS**.  
It is designed to reinforce modern JavaScript concepts such as **object destructuring, default parameters, DOM manipulation, event handling, data filtering, and array methods**.

The UI allows users to **filter players by role or nickname** using a dropdown menu, dynamically updating the displayed player cards.

---

## 🚀 Project Features

- Displays football team metadata (team name, sport, year, head coach)
- Dynamically renders player cards from a JavaScript data structure
- Filters players by:
  - All players
  - Nicknames only
  - Position (Forward, Midfielder, Defender)
- Uses modern JavaScript best practices
- Fully responsive layout
- No external libraries or frameworks required

---

## 🧠 Concepts Covered

This project reinforces the following JavaScript concepts:

- **DOM Manipulation**
- **Object & Nested Object Structures**
- **Object Destructuring**
- **Default Function Parameters**
- **Array Methods**
  - `map()`
  - `filter()`
  - `join()`
- **Event Handling**
- **Switch Statements**
- **Ternary Operators**
- **Immutability using `Object.freeze()`**

---


---

## 🏗️ How the Project Works

### 1️⃣ Data Structure
All team and player data is stored in a single immutable object:

```js
const myFavoriteFootballTeam = {
  team: "Argentina",
  sport: "Football",
  year: 1986,
  isWorldCupWinner: true,
  headCoach: {
    coachName: "Carlos Bilardo",
    matches: 7
  },
  players: [ ... ]
};

