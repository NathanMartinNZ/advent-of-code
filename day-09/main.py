
with open("input.txt") as f:
    lines = f.readlines()
    movements = []
    for line in lines:
        x, y = line.replace("\n", "").split(" ")
        movements.append([x, int(y)]) 

print(movements)