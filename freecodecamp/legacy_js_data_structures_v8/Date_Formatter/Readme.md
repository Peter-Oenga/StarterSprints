# 📅 Date Formatter Project (JavaScript Date Object)

## 📌 Project Overview

This project demonstrates how to work with the **JavaScript `Date` object** by building a simple and interactive **date formatter**.  
Users can select different date formats from a dropdown menu, and the application dynamically displays the current date based on their selection.

All **HTML and CSS** are pre-provided. The focus of this project is on **JavaScript logic**, including working with dates, event handling, string manipulation, and conditional logic.

---

## 🎯 Learning Objectives

By completing this project, you will learn how to:

- Use the JavaScript **`Date` constructor**
- Extract date values using:
  - `getDate()`
  - `getMonth()`
  - `getFullYear()`
  - `getHours()`
  - `getMinutes()`
- Format dates using **template literals**
- Manipulate strings with:
  - `split()`
  - `reverse()`
  - `join()`
- Handle user input with the **`change` event**
- Implement logic using a **`switch` statement**
- Update the DOM using `textContent`

---


---

## ⚙️ How the Project Works

### 1. DOM Element Selection

The project starts by selecting required elements from the DOM:

- `#current-date` → Displays the formatted date
- `#date-options` → Dropdown menu for selecting date format

---

### 2. Creating a Date Object

A new `Date` object is created using:

```js
new Date();


