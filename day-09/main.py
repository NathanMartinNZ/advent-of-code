
with open("input.txt") as f:
    lines = f.readlines()
    movements = []
    for line in lines:
        x, y = line.replace("\n", "").split(" ")
        movements.append([x, int(y)]) 

### PART 1 ###
positions = [[0, 0] for i in range(2)] # Starts as bottom right [x, y]
tail_visits = []

def move_head(direction, steps):
    match direction:
        case "U":
            positions[0][1] = positions[0][1] + 1
        case "R":
            positions[0][0] = positions[0][0] + 1
        case "D":
            positions[0][1] = positions[0][1] - 1
        case "L":
            positions[0][0] = positions[0][0] - 1

    move_tail(1) # 1 is the order behind the head

    steps = steps - 1
    if steps > 0:
        move_head(direction, steps)

def move_tail(tail_idx):
    pos_diff = [h - t for h, t in zip(positions[tail_idx-1], positions[tail_idx])]

    if pos_diff[1] == 2:
        # UP
        positions[tail_idx][0] = positions[tail_idx-1][0]
        positions[tail_idx][1] = positions[tail_idx-1][1] - 1
    elif pos_diff[0] == 2:
        # RIGHT
        positions[tail_idx][0] = positions[tail_idx-1][0] - 1
        positions[tail_idx][1] = positions[tail_idx-1][1]
    elif pos_diff[1] == -2:
        # DOWN
        positions[tail_idx][0] = positions[tail_idx-1][0]
        positions[tail_idx][1] = positions[tail_idx-1][1] + 1
    elif pos_diff[0] == -2:
        # LEFT
        positions[tail_idx][0] = positions[tail_idx-1][0] + 1
        positions[tail_idx][1] = positions[tail_idx-1][1] 

    
    if positions[tail_idx] not in tail_visits:
        tail_visits.append(positions[tail_idx].copy())


for movement in movements:
    move_head(movement[0], movement[1])

part_1_answer = len(tail_visits)
print(part_1_answer)



### PART 2 ###
positions = [[0, 0] for i in range(10)] # Starts as bottom right [x, y]
tail_visits = []
last_tail_idx = len(positions) - 1

def move_head(direction, steps):
    match direction:
        case "U":
            positions[0][1] = positions[0][1] + 1
        case "R":
            positions[0][0] = positions[0][0] + 1
        case "D":
            positions[0][1] = positions[0][1] - 1
        case "L":
            positions[0][0] = positions[0][0] - 1

    for idx in range(1, last_tail_idx+1):
        move_tail(idx)

    steps = steps - 1
    if steps > 0:
        move_head(direction, steps)

def move_tail(tail_idx):
    pos_diff = [h - t for h, t in zip(positions[tail_idx-1], positions[tail_idx])]
    new_x = positions[tail_idx][0]
    new_y = positions[tail_idx][1]
    x_updated, y_updated = (False, False)

    if pos_diff[1] == 2:
        # UP
        if not x_updated: new_x = positions[tail_idx-1][0]
        new_y = positions[tail_idx-1][1] - 1
        y_updated = True
    if pos_diff[0] == 2:
        # RIGHT
        new_x = positions[tail_idx-1][0] - 1
        if not y_updated: new_y = positions[tail_idx-1][1]
        x_updated = True
    if pos_diff[1] == -2:
        # DOWN
        if not x_updated: new_x = positions[tail_idx-1][0]
        new_y = positions[tail_idx-1][1] + 1
        y_updated = True
    if pos_diff[0] == -2:
        # LEFT
        new_x = positions[tail_idx-1][0] + 1
        if not y_updated: new_y = positions[tail_idx-1][1]
        x_updated = True
    
    positions[tail_idx] = [new_x, new_y]

    if tail_idx == last_tail_idx and positions[tail_idx] not in tail_visits:
        tail_visits.append([new_x, new_y])


for movement in movements:
    move_head(movement[0], movement[1])

part_2_answer = len(tail_visits)
print(part_2_answer)