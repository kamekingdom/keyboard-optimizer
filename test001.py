import random

# キーボードの配列を作成
keyboard = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']
]

# 座標の初期化(小指以外の8本指)
my_fingers = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 6], [1, 7], [1, 8], [1, 9]]

def find_key(key, input_keyboard):
    for i in range(len(input_keyboard)):
        for j in range(len(input_keyboard[i])):
            if input_keyboard[i][j] == key:
                return (i, j)
    return None

def calculate_cost(word, input_keyboard):
    cost = 0
    print(f"key:0 [[0, 0]] {my_fingers}")
    for key in word:
        key_position = find_key(key, input_keyboard)
        if key_position is not None:
            min_distance = float('inf')
            for i in range(len(my_fingers)):
                distance = abs(my_fingers[i][0] - key_position[0]) + abs(my_fingers[i][1] - key_position[1])
                if distance < min_distance:
                    min_distance = distance
                    chosen_finger = i
            cost += min_distance
            # 移動した場所を保存
            my_fingers[chosen_finger] = list(key_position)
            print(f"key:{key} [{list(key_position)}] {my_fingers}")
    print(f"cost: {cost}")
    return cost

def generate_random_keyboard():
    # ランダムなキーボード配列を生成
    random_keyboard = keyboard.copy()
    for i in range(len(keyboard)):
        random.shuffle(random_keyboard[i])
    return random_keyboard

def optimize_keyboard_layout():
    best_keyboard = [0,0]
    best_cost = float("inf")

    for _ in range(100):
        random_keyboard = generate_random_keyboard()
        cost = calculate_cost(word, random_keyboard)
        if cost < best_cost:
            best_cost = cost
            best_keyboard = random_keyboard

    return best_keyboard, cost

# ランダムな単語を生成（ここではシンプルに'WORD'とする）
word = 'WORD'
best_keyboard, best_cost = optimize_keyboard_layout()
print(f'The best keyboard layout for typing the word "{word}" is:')
for row in best_keyboard:
    print(row)
print(f"best cost: {best_cost}")