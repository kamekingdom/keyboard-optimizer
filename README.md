# 🄤 Keyboard Optimizer

**An interactive tool that dynamically optimizes keyboard layouts based on user-specific typing speed and finger travel cost.**  
This project measures your response time for each key and rearranges the keyboard to minimize typing effort and maximize input efficiency, especially for English words.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Algorithm Overview](#algorithm-overview)
- [Usage Instructions](#usage-instructions)
- [Requirements](#requirements)
- [Applications](#applications)
- [Example Output](#example-output)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## 🥸 Overview

**Keyboard Optimizer** is a customizable and experimental system that:

- Measures how fast you can press each key on a keyboard
- Calculates finger travel cost based on keyboard layout and hand positions
- Learns from your typing behavior and English word usage
- Suggests an optimized keyboard layout that reduces movement and boosts reaction time

---

## 🌟 Features

- ⌨️ Measures individual keypress response times (e.g., `{a: 0.24, b: 0.38, ...}`)
- 🔁 Calculates and updates keyboard layout dynamically based on:
  - Finger movement distance
  - Frequency of specific finger use
  - Word usage frequency (common English words prioritized)
- 🧐 Assigns high-priority letters (`E, T, A, O, I, N, S, H`) to the fastest-access keys
- 🔄 Evaluates and updates the layout until movement cost converges

---

## 🧲 Algorithm Overview

- **Initial layout:**

```python
keyboard = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
]
```

- **Finger movement cost:**
```text
cost = abs(row1 - row2) + abs(col1 - col2)
```

### Optimization Process

1. Random English words are displayed
2. User types each key; system records:
   - Reaction time per key (`{a: 0.2, b: 0.4, ...}`)
   - Transition time between keys (`a → b = 0.3s`)
3. Letters with higher delay are moved closer to home position
4. High-priority letters (`E, T, A, O, I, N, S, H`) are placed in fastest positions
5. Layout is iteratively optimized until cost stabilizes

---

## 🚀 Usage Instructions

1. Run the program (terminal or GUI)
2. Type the displayed random characters as fast as possible
3. All keypress times are recorded and sorted
4. Optimized layout will be printed when the system converges

---

## 🧰 Requirements

- Python 3.x
- Uses only standard libraries:
  - `random`
  - `time`
  - `collections`

> *(Optional: For GUI-based visualization, you can integrate `tkinter` or `pygame`)*

---

## 💡 Applications

- Custom keyboard layouts for power typists
- Ergonomic optimization tools
- Accessibility research
- Interactive typing trainers

---

## 📈 Example Output

```bash
Key Press Time (seconds):
{'e': 0.21, 't': 0.26, 'a': 0.30, 'b': 0.45, 'z': 0.52, ...}

Optimized Layout:
[['T', 'E', 'A', 'O', 'I', 'N', 'S', 'H', ...],
 ['...', ...],
 ['...', ...]]
```

---

## 🧠 Future Improvements

- Session-based adaptive learning
- Language-specific layout tuning (e.g. for Japanese or French)
- Mechanical keyboard firmware integration
- Finger path heatmaps and visual stats

---

## 📄 License

This project is licensed under the MIT License.

---

Created with ⚙️ and ⌨️ by [@kamekingdom](https://github.com/kamekingdom)
