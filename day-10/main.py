

with open("input.txt") as f:
    lines = f.readlines()
    instructions = []
    for line in lines:
        line = line.replace("\n", "").split(" ")
        x = line[0]
        y = int(line[1]) if len(line) > 1 else ""
        instructions.append([x, y])

### PART 1 ###
CYCLE_HIST = [[1, 1]]
X = 1

for instruction in instructions:
    CYCLE_HIST.append([X, X])

    if instruction[0] != "noop":
        new_x = X + instruction[1]
        CYCLE_HIST.append([X, new_x])
        X += instruction[1]


idx_filter = [CYCLE_HIST[i][0] * (i) for i in [20, 60, 100, 140, 180, 220]]
part_1_answer = sum(idx_filter)

print(part_1_answer)


### PART 2 ###
X = 1
SPRITE_POS = ["#", "#", "#"] + ["." for _ in range(37)]
CURR_CRT_ROW = 0  # Max 5
CRT_ROWS = [[] for _ in range(6)]

for instruction in instructions:
    # Go to next CRT row if at end
    if len(CRT_ROWS[CURR_CRT_ROW]) >= 40:
        CURR_CRT_ROW += 1

    # Draw CRT pixel
    if SPRITE_POS[len(CRT_ROWS[CURR_CRT_ROW])] == "#":
        CRT_ROWS[CURR_CRT_ROW].append("#")
    else:
        CRT_ROWS[CURR_CRT_ROW].append(".")

    # If addx, run another cycle
    if instruction[0] != "noop":
        # Go to next CRT row if at end
        if len(CRT_ROWS[CURR_CRT_ROW]) >= 40:
            CURR_CRT_ROW += 1

        # Increment X
        X += instruction[1]

        # Draw CRT pixel
        if SPRITE_POS[len(CRT_ROWS[CURR_CRT_ROW])] == "#":
            CRT_ROWS[CURR_CRT_ROW].append("#")
        else:
            CRT_ROWS[CURR_CRT_ROW].append(".")

        # Set sprite position
        NEW_SPRITE_POS = ["." for _ in range(40)]
        if X-1 < 40:
            NEW_SPRITE_POS[X-1] = "#"
        if X < 40:
            NEW_SPRITE_POS[X] = "#"
        if X+1 < 40:
            NEW_SPRITE_POS[X+1] = "#"
        SPRITE_POS = NEW_SPRITE_POS

# Part 2 answer
for ROW in CRT_ROWS:
    print(''.join(ROW))
