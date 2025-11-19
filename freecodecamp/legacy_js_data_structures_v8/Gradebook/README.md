# 📘 Gradebook Mini Project

This project is a simple JavaScript exercise designed to help you review **core fundamentals** such as functions, loops, conditionals, arrays, and return values.  
You will gradually build a small gradebook that calculates averages, assigns letter grades, and evaluates student performance.

---

## 🚀 Features

### ✔ **getAverage(scores)**  
Calculates the class average from an array of numeric scores.

```js
function getAverage(scores) {
  let sum = 0;

  for (const score of scores) {
    sum += score;
  }

  return sum / scores.length;
}
