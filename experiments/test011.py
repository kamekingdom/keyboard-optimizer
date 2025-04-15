# QWERTY配列の定義
qwerty_layout = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']
]

# QWERTY配列を表示
print()
for row in qwerty_layout:
    print(' '.join(row))
print()