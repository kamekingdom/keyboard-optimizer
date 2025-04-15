import random
import copy
from collections import Counter
import matplotlib.pyplot as plt

# generate_japanese_words モジュールの読み込み（相対パス対応）
from frequent_words.generate_japanese_words import input_text

# ANSIカラーコード（赤）
RED = "\033[31m"
RESET = "\033[0m"

# キーボードのレイアウト
keyboard_layout = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']
]

# 指の初期位置（左4本 + 右4本）※親指除く
initial_finger_positions = [[1, 0], [1, 1], [1, 2], [1, 3],
                            [1, 6], [1, 7], [1, 8], [1, 9]]

# 指の重み（疲れやすさ）
finger_weights = [1.0, 0.9, 0.8, 0.7, 0.7, 0.8, 0.9, 1.0]

# キー位置マップを構築
def build_key_position_map(layout):
    return {key: (r, c) for r, row in enumerate(layout) for c, key in enumerate(row)}

# タイピングコストを計算
def calculate_typing_cost(word, layout):
    key_pos_map = build_key_position_map(layout)
    total_cost = 0
    finger_positions = copy.deepcopy(initial_finger_positions)
    for key in word:
        key_position = key_pos_map.get(key)
        if key_position:
            min_cost = float('inf')
            for i, pos in enumerate(finger_positions):
                dist = abs(pos[0] - key_position[0]) + abs(pos[1] - key_position[1])
                cost = dist * finger_weights[i]
                if cost < min_cost:
                    min_cost = cost
                    chosen_finger = i
            total_cost += min_cost
            finger_positions[chosen_finger] = list(key_position)
    return total_cost

# ランダムレイアウト生成
def generate_random_keyboard_layout():
    flat = sum(copy.deepcopy(keyboard_layout), [])
    random.shuffle(flat)
    return [flat[i:i+10] for i in range(0, len(flat), 10)]

# 2点交叉
def crossover(parent1, parent2):
    flat1 = sum(parent1, [])
    flat2 = sum(parent2, [])
    start, end = sorted(random.sample(range(len(flat1)), 2))
    subset = flat1[start:end]
    remainder = [k for k in flat2 if k not in subset]
    combined = remainder[:start] + subset + remainder[start:]
    return [combined[i:i+10] for i in range(0, len(combined), 10)]

# 突然変異
def mutate(layout):
    layout_copy = copy.deepcopy(layout)
    for _ in range(100):
        r1, r2 = random.choices(range(len(layout_copy)), k=2)
        c1 = random.choice(range(len(layout_copy[r1])))
        c2 = random.choice(range(len(layout_copy[r2])))
        if (r1, c1) != (r2, c2):
            layout_copy[r1][c1], layout_copy[r2][c2] = layout_copy[r2][c2], layout_copy[r1][c1]
            return layout_copy
    return layout_copy  # fallback

# 最適化アルゴリズム（エリート選択＋交叉＋突然変異）
def optimize_keyboard_layout(word, population_num=100, generation_num=1000):
    population = [generate_random_keyboard_layout() for _ in range(population_num)]
    population.sort(key=lambda l: calculate_typing_cost(word, l))
    cost_history = []

    for gen in range(generation_num):
        parents = sorted(population[:20], key=lambda l: calculate_typing_cost(word, l))[:2]
        child = crossover(parents[0], parents[1])
        child = mutate(child)
        cost = calculate_typing_cost(word, child)
        if cost < calculate_typing_cost(word, parents[0]):
            population.remove(parents[0])
            population.append(child)
        population.sort(key=lambda l: calculate_typing_cost(word, l))
        print(f"Generation: {gen}, Cost: {cost:.2f}")
        cost_history.append(cost)

    return population[0], calculate_typing_cost(word, population[0]), cost_history

# レイアウトの表示
def print_layout(layout, highlight_word):
    for row in layout:
        for key in row:
            print((RED + key + RESET) if key in highlight_word else key, end=' ')
        print()
    print()

# グラフ表示
def plot_cost_history(cost_history):
    plt.plot(cost_history)
    plt.xlabel("Generation")
    plt.ylabel("Typing Cost")
    plt.title("Typing Cost Optimization")
    plt.grid(True)
    plt.show()

# 実行部分
if __name__ == "__main__":
    word_to_optimize = input_text.upper()
    best_layout, best_cost, cost_history = optimize_keyboard_layout(word_to_optimize)

    print(f'\nOptimized keyboard layout for word "{word_to_optimize}":\n')
    print_layout(best_layout, word_to_optimize)
    print(f"Final Cost: {best_cost:.2f}")

    plot_cost_history(cost_history)
