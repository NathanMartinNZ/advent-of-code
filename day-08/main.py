import math

with open("input.txt") as f:
    lines = f.readlines()
    grid = [[int(num) for num in [*line.replace("\n", "")]] for line in lines]


### Part 1 ###
visible_count = 0
invisible_count = 0

for r, row in enumerate(grid):

    for c, tree in enumerate(row):
        visible = True
        # NOT VISIBLE IF AT LEAST 1 TREE IS HIGHER IN ALL DIRECTIONS
        # Inside bounds
        if c != 0 and c != len(row)-1 and r != 0 and r != len(grid)-1:
            left = row[:c]
            right = row[c+1:]
            up = [g[c] for g in grid[:r]]
            down = [g[c] for g in grid[r+1:]]

            left.sort(reverse=True)
            right.sort(reverse=True)
            up.sort(reverse=True)
            down.sort(reverse=True)

            if left[0] >= tree and right[0] >= tree and up[0] >= tree and down[0] >= tree:
                visible = False

        if visible:
            visible_count += 1
        else:
            invisible_count += 1

part_1_answer = visible_count
print(part_1_answer)


### Part 2 ###
all_visibility_scores = []

for r, row in enumerate(grid):
    for c, tree in enumerate(row):
        left = row[:c] if c != 0 else [0]
        right = row[c+1:] if c != len(row)-1 else [0]
        up = [g[c] for g in grid[:r]] if r != 0 else [0]
        down = [g[c] for g in grid[r+1:]] if r != len(grid)-1 else [0]

        left.reverse()
        up.reverse()

        left_vis_count = 0
        for l in left:
            left_vis_count += 1
            if l >= tree:
                break

        right_vis_count = 0
        for ri in right:
            right_vis_count += 1
            if ri >= tree:
                break

        up_vis_count = 0
        for u in up:
            up_vis_count += 1
            if u >= tree:
                break

        down_vis_count = 0
        for d in down:
            down_vis_count += 1
            if d >= tree:
                break

        all_visibility_scores.append(
            math.prod([left_vis_count, right_vis_count, up_vis_count, down_vis_count]))

part_2_answer = max(all_visibility_scores)
print(part_2_answer)
