def print_towers(towers):
    for tower in towers:
        print(tower)
    print()

def move_disk(towers, from_tower, to_tower):
    for i in range(len(towers[from_tower])):
        if towers[from_tower][i] != 0:
            disk = towers[from_tower][i]
            towers[from_tower][i] = 0
            break


    for i in range(len(towers[to_tower]) - 1, -1, -1):
        if towers[to_tower][i] == 0:
            towers[to_tower][i] = disk
            break

def game(n, from_tower, to_tower, aux_tower, towers):
    if n == 1:
        move_disk(towers, from_tower, to_tower)
        print_towers(towers)
        return
    game(n - 1, from_tower, aux_tower, to_tower, towers)
    move_disk(towers, from_tower, to_tower)
    print_towers(towers)
    game(n - 1, aux_tower, to_tower, from_tower, towers)

towers = [
    [1, 2, 3, 4],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print("Startposition:")
print_towers(towers)

game(4, 0, 2, 1, towers)
