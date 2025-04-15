# 🔤 Keyboard Optimizer

**An interactive tool that dynamically optimizes keyboard layouts based on user-specific typing speed and finger travel cost.**  
This project measures your response time for each key and rearranges the keyboard to minimize typing effort and maximize input efficiency, especially for English words.

---

## 📌 Overview

Keyboard Optimizer is a customizable and experimental system that:

- Measures how fast you can press each key on a keyboard
- Calculates finger travel cost based on keyboard layout and hand positions
- Learns from your typing behavior and English word usage
- Suggests an optimized keyboard layout that reduces movement and boosts reaction time

---

## ⚙️ Key Features

- ⌨️ Measures individual keypress response times (e.g., `{a: 0.24, b: 0.38, ...}`)
- 🔁 Calculates and updates keyboard layout dynamically based on:
  - Finger movement distance
  - Frequency of specific finger use
  - Word usage frequency (common English words prioritized)
- 🧠 Assigns high-priority letters (`E, T, A, O, I, N, S, H`) to the fastest-access keys
- 🔄 Evaluates and updates the layout until movement cost converges

---

## 🧮 Algorithm Overview

- Initial layout:
```python
keyboard = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
]
