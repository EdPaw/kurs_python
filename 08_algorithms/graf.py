
#dom, kosciol, kino, bar, szkola, szpital, teatr
miasto = [
    [0, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1],
    [1, 2, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0]
]

miejsca = ['dom', 'kosciol', 'kino', 'bar', 'szkola', 'szpital', 'teatr']

for i, row in enumerate(miasto):
    for j, value in enumerate(row):
        if value == 1:
            print(f"{miejsca[i]} - {miejsca[j]}")
