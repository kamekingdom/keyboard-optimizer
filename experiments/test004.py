### 変更点 ###
# グラフ表示機能を追加
# トーナメント選択＆一様交叉


import random
import copy
from collections import Counter
import matplotlib.pyplot as plt

# キーボードのレイアウトを配列で作成
keyboard_layout = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']
]

# 指の番号と指の対応関係の辞書
finger_names = {
    0: '左小指',
    1: '左薬指',
    2: '左中指',
    3: '左人差し指',
    4: '右人差し指',
    5: '右中指',
    6: '右薬指',
    7: '右小指'
}

# 8本の指の初期位置（親指は除く）
initial_finger_positions = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 6], [1, 7], [1, 8], [1, 9]]

# 指の重み付け
# 人差し指　＞　中指 ＞　薬指　＞　小指
finger_weights = [1.0, 0.9, 0.8, 0.7, 0.7, 0.8, 0.9, 1.0]

# キーの位置を探す関数
def find_key_position(key, layout):
    for row_index in range(len(layout)):
        for column_index in range(len(layout[row_index])):
            if layout[row_index][column_index] == key:
                return (row_index, column_index)
    return None

# タイピングコストを計算する関数
def calculate_typing_cost(word, layout):
    total_cost = 0
    finger_moves = []
    finger_positions = copy.deepcopy(initial_finger_positions)
    for key in word:
        key_position = find_key_position(key, layout)
        if key_position is not None:
            min_distance = float('inf')
            for i in range(len(finger_positions)):
                distance = abs(finger_positions[i][0] - key_position[0]) + abs(finger_positions[i][1] - key_position[1])
                weighted_distance = distance * finger_weights[i]
                if weighted_distance < min_distance:
                    min_distance = weighted_distance
                    chosen_finger_index = i
            total_cost += min_distance
            finger_moves.append((finger_names[chosen_finger_index], key))
            finger_positions[chosen_finger_index] = list(key_position)
    return total_cost, finger_moves

# ランダムなキーボードレイアウトを生成する関数
def generate_random_keyboard_layout():
    random_layout = copy.deepcopy(keyboard_layout)
    flattened = sum(random_layout, [])
    random.shuffle(flattened)
    return [flattened[n:n+10] for n in range(0, len(flattened), 10)]

# 二つの親から新しいキーボードレイアウトを生成する関数
def crossover(parent1, parent2):
    parent1_flat = sum(parent1, [])
    parent2_flat = sum(parent2, [])
    subset = random.sample(parent1_flat, len(parent1_flat) // 2)
    remainder = [key for key in parent2_flat if key not in subset]
    new_layout_flat = subset + remainder
    return [new_layout_flat[i:i+10] for i in range(0, len(new_layout_flat), 10)]

# レイアウトを突然変異させる関数
def mutate(layout):
    layout_copy = copy.deepcopy(layout)
    while True:
        row1, row2 = random.choices(range(len(layout_copy)), k=2)
        col1 = random.choice(range(len(layout_copy[row1])))
        col2 = random.choice(range(len(layout_copy[row2])))
        if row1 != row2 or col1 != col2:
            break
    layout_copy[row1][col1], layout_copy[row2][col2] = layout_copy[row2][col2], layout_copy[row1][col1]
    return layout_copy

# キーボードレイアウトを最適化する関数
def optimize_keyboard_layout(word_to_optimize):
    population_num = 100
    generation_num = 1000
    population = [generate_random_keyboard_layout() for _ in range(population_num)]
    population.sort(key=lambda layout: calculate_typing_cost(word_to_optimize, layout)[0])

    # コストの推移を記録するリスト
    cost_history = []

    for generation in range(generation_num):
        parent_layouts = random.choices(population[:20], k=2)
        child_layout = crossover(parent_layouts[0], parent_layouts[1])
        child_layout = mutate(child_layout)
        now_cost = calculate_typing_cost(word_to_optimize, child_layout)[0]
        if now_cost < calculate_typing_cost(word_to_optimize, parent_layouts[0])[0]:
            population.remove(parent_layouts[0])
            population.append(child_layout)
        population.sort(key=lambda layout: calculate_typing_cost(word_to_optimize, layout)[0])
        print(f"Generation: {generation} cost: {now_cost}")
        cost_history.append(now_cost)

    best_layout = population[0]
    best_cost, best_moves = calculate_typing_cost(word_to_optimize, best_layout)
    return best_layout, best_cost, best_moves, cost_history

# ユーザーに最適化したい単語を入力させる
word_to_optimize = input("最適化したい単語を入力してください >> ").upper()

best_layout, best_cost, best_moves, cost_history = optimize_keyboard_layout(word_to_optimize)

# ANSIエスケープコード
RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"

# キーボードレイアウトを表示する関数
def print_layout(layout, highlight_key=None):
    for row in layout:
        for key in row:
            if key in word_to_optimize:
                if key == highlight_key:
                    print(BLUE + key + RESET, end=' ')
                else:
                    print(RED + key + RESET, end=' ')
            else:
                print(key, end=' ')
        print()
    print()

# 折れ線グラフでコストの推移を表示する関数
def plot_cost_history(cost_history):
    plt.plot(cost_history)
    plt.xlabel("Generation")
    plt.ylabel("Cost")
    plt.title("Typing Cost Optimization")
    plt.show()

print(f'単語"{word_to_optimize}"をタイプする最適なキーボードレイアウトは以下のとおりです：\n')
print_layout(best_layout)
print(f"最適コスト: {best_cost}")
print(f"最適な移動: {best_moves}")
print("動かし方")
for move in best_moves:
    print(f'次に押すキー: {move[1]}')
    print_layout(best_layout, highlight_key=move[1])
    input("Enterを押して次に進む")

# コストの推移をグラフで表示
plot_cost_history(cost_history)
