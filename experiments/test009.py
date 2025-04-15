### 変更点 ###
# 選択方法をトーナメント選択
# 交叉方法を一様交叉
# 頻出英単語500単語でqwerty配列になるかテストしてみる

import random
import copy
from collections import Counter
import matplotlib.pyplot as plt

keyboard_layout = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']
]

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

initial_finger_positions = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 6], [1, 7], [1, 8], [1, 9]]

finger_weights = [1.0, 0.9, 0.8, 0.7, 0.7, 0.8, 0.9, 1.0]

def find_key_position(key, layout):
    for row_index in range(len(layout)):
        for column_index in range(len(layout[row_index])):
            if layout[row_index][column_index] == key:
                return (row_index, column_index)
    return None

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

def generate_random_keyboard_layout():
    random_layout = copy.deepcopy(keyboard_layout)
    flattened = sum(random_layout, [])
    random.shuffle(flattened)
    return [flattened[n:n+10] for n in range(0, len(flattened), 10)]

def crossover(parent1, parent2):
    parent1_flat = sum(parent1, [])
    parent2_flat = sum(parent2, [])
    new_layout_flat = [random.choice([p1, p2]) for p1, p2 in zip(parent1_flat, parent2_flat)]
    
    # Make sure all keys are unique
    if len(set(new_layout_flat)) != len(new_layout_flat):
        return None

    return [new_layout_flat[i:i+10] for i in range(0, len(new_layout_flat), 10)]

def mutate(layout):
    layout_copy = copy.deepcopy(layout)
    while True:
        row1, row2 = random.choices(range(len(layout_copy)), k=2)
        col1 = random.choice(range(len(layout_copy[row1])))
        col2 = random.choice(range(len(layout_copy[row2])))
        if row1 != row2 or col1 != col2:
            break
    layout_copy[row1][col1], layout_copy[row2][col2] = layout_copy[row2][col2], layout_copy[row1][col1]
    
    # Make sure all keys are unique
    if len(set(sum(layout_copy, []))) != len(sum(layout_copy, [])):
        return None

    return layout_copy


# Tournament selection
def tournament_selection(population, tournament_size):
    tournament = random.choices(population, k=tournament_size)
    tournament.sort(key=lambda layout: calculate_typing_cost(word_to_optimize, layout)[0])
    return tournament[0]

def optimize_keyboard_layout(word_to_optimize):
    population_num = 100
    generation_num = 1000
    tournament_size = 20  # Tournament size
    population = [generate_random_keyboard_layout() for _ in range(population_num)]
    population.sort(key=lambda layout: calculate_typing_cost(word_to_optimize, layout)[0])

    cost_history = []

    for generation in range(generation_num):
        while True:
            parent1 = tournament_selection(population, tournament_size)
            parent2 = tournament_selection(population, tournament_size)
            child_layout = crossover(parent1, parent2)
            if child_layout is None:
                continue
            child_layout = mutate(child_layout)
            if child_layout is None:
                continue
            break
        now_cost = calculate_typing_cost(word_to_optimize, child_layout)[0]
        if now_cost < calculate_typing_cost(word_to_optimize, parent1)[0]:
            population.remove(parent1)
            population.append(child_layout)
        population.sort(key=lambda layout: calculate_typing_cost(word_to_optimize, layout)[0])
        print(f"Generation: {generation} cost: {now_cost}")
        cost_history.append(now_cost)

    best_layout = population[0]
    best_cost, best_moves = calculate_typing_cost(word_to_optimize, best_layout)
    return best_layout, best_cost, best_moves, cost_history

result = "nowonidetetahashitogasaisurureeirumokotonakarareruyouarunaitteyatachikisonotameraremesenatsutsunezumierinnonokedayotsuunaruiusutarirukanadoorimuworinurarihyonganiyoriworuheseruwaremimazubininomonochideshishimauoyajinakuarikakebesannarishitadekirujimananiruworakononoridassoreraoniikubageshiitsumadedakerareruwotsukaresoudekihodonireatsuerunagarakerunomishiyoumataniiikuketayoruidenanihainakattsuketsuihaniworenienierushinonenekotaishigerukoshitokorogakenitedeetsunohaairrishigarigatsunikuterunurikabetanigakubuetakerahatonotodarumawonotobbaredetsuwarerugerushimasshikatadewaasaraniniragaranaratomoshimaihananishinijimechanchankoshikugaruteggaiguhademounochitaawariimetoinoorokuronokishimitorikashiharitadajiruwobakurewasegiitsumarederegareheruarasujikanametoshiokedousokobakeshimekatsutetereshikashiroutonijiranadenutsurubekorewakkirutounoshitsukikunigotoreimamayatsumotokosugashideratorerinshitoiirashianonigatsunogashibarerutokenokehotondooutochanhakutaratontagazuchiwarariigankoutekesasetojiharakirrisumotsukareruhatachimatsumorattokinopperabouoyobikakerumokuteekasuikekekeamariyamakaramakirejikudesutanahakkuruwarumooerayoganaminokasandetakunorekirioukunokikkakegetaharesarakkishikokokasenaahadakawausonakunayyaadekebetamoshikimareichikanarinotsuoidekuhayayarikushikarashitsugauchihokaigaseishiniyukimasukikusarasokkurinoimashitekagakisorezoreyashiiyanaonashiorabekuimihakehashigobasugatsuseyoubotonariyokutsukeruashimasekonobigatayarumowotaremoraukisuhitoyayariminakerejitatorusoshitejijiiheriimakakatsumishikugasugunisekauitodarigashadokurobakarinichimaboroshigarerushiitoodokotadashikarasarashikutekiiiinmarushikemoretokumikibouburinigaiteranukiodoroodorokanimagarinyuukurerugamekararishimokarakutomemarinonderumukukikenijirashiihahakunkesanigemuniyatohoboruritoraunotsutoshirishimerukuroonnautomubabaashikakezuishibarakukainareruyoukaitobetabikitatekuudeshimaishimorinayagayazutsumoisaserunatohideriuniimuyuenitsuuupekukokeshizetobakakarusudenihesaniwadaijarashoukerakerakariikikuitowazukikinagaheshibekijimehakaradotsunatamomotsuiwayurutorashiuneri"
word_to_optimize = result.upper()

best_layout, best_cost, best_moves, cost_history = optimize_keyboard_layout(word_to_optimize)

RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"

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

"""
print("動かし方")
for move in best_moves:
    print(f'次に押すキー: {move[1]}')
    print_layout(best_layout, highlight_key=move[1])
    input("Enterを押して次に進む")
"""
    
plot_cost_history(cost_history)
