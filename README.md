# Keyboard Layout Optimizer (2022)

A Python-based optimization tool that evolves keyboard layouts to minimize finger movement cost when typing common words in either **English** or **Japanese**.

---

## Overview

This project uses **genetic algorithms** to generate and evolve keyboard layouts that reduce typing effort. It supports both English and Japanese input optimization based on frequent word usage.

---

## Features

- Supports **two languages**: English and Japanese
- **Elite selection** and **two-point crossover** genetic algorithm
- Customizable keyboard layouts and finger weights
- Visual typing cost graph over generations
- Modular structure with separate input sources

---

## Project Structure

```
keyboard-optimizer/
├── data/                         # Input word datasets
├── experiments/                 # Experimental code and logs
├── frequent_words/             # Word generators per language
│   ├── generate_english_words.py
│   └── generate_japanese_words.py
├── generation_en.py            # Main script for English optimization
├── generation_jp.py            # Main script for Japanese optimization
├── calculate_similarity.py    # (Optional) Experimental similarity calc
├── README.md                   # This file
```

---

## Getting Started

### 1. Install Dependencies
```bash
pip install matplotlib
```

### 2. Run English Keyboard Optimizer
```bash
python generation_en.py
```

### 3. Run Japanese Keyboard Optimizer
```bash
python generation_jp.py
```

> You'll be prompted to input a word. The optimizer will search for the lowest typing cost layout over generations.

---

## Output Example

```
Optimized keyboard layout for word "EXAMPLE":

Q W E R T Y U I O P
A S D F G H J K L ;
Z X C V B N M , . /

Final Cost: 12.34
```

- Typing cost is computed by weighted finger travel distance.
- Cost transition over time is shown as a graph (via matplotlib).

---

## Future Plans

- Sentence-level optimization
- Export optimized layouts (JSON / PNG)
- Heatmap visualization of usage
- Integration with real-time key press measurement

---

## License

MIT License

---

Created by [@kamekingdom](https://github.com/kamekingdom)
