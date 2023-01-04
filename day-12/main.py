
with open("input.txt") as f:
    lines = [list(line.replace("\n", "").strip()) for line in f.readlines()]
    lines = [[ord(l) for l in line] for line in lines]

    # Part 1
    start = 0
    end = 0
    # Part 2
    starts = []

    for idx in range(len(lines)):
        for i, val in enumerate(lines[idx]):
            if val == ord("a"):
                starts.append([i, idx])
            elif val == ord("S"):
                lines[idx][i] = ord("a")
                start = [i, idx]
                starts.append(start)
            elif val == ord("E"):
                lines[idx][i] = ord("z")
                end = [i, idx]


### Part 1 & 2 ###
rows = len(lines[0])
cols = len(lines)

def next_move(x, y):
    # [L, R, U, D]
    return [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]

def shortest_path(lines, start, end):
    searching_paths = [[start]]
    visited_coords = [start]
    
    while searching_paths != []:
        curr_path = searching_paths.pop(0)
        curr_coord = curr_path[-1]
        
        curr_x, curr_y = curr_coord
        
        if curr_coord == end:
            return curr_path
        
        for next_coord in next_move(curr_x, curr_y):
            nextX, nextY = next_coord
            
            # Skip if invalid
            if nextX < 0 or nextX >= rows or \
               nextY < 0 or nextY >= cols or \
               next_coord in visited_coords or \
               (lines[nextY][nextX] - lines[curr_y][curr_x]) > 1:
                continue
            
            searching_paths.append(curr_path + [next_coord])
            visited_coords += [next_coord]


min_path_distance = shortest_path(lines, start, end)
part_1_answer = len(min_path_distance) - 1
print(part_1_answer)

min_path_distance_p2 = 0
for s in starts:
    sp = shortest_path(lines, s, end)
    # None means path couldn't make the end
    if sp is not None:
        if min_path_distance_p2 == 0:
            min_path_distance_p2 = len(sp)
        elif len(sp) < min_path_distance_p2:
            min_path_distance_p2 = len(sp)
part_2_answer = min_path_distance_p2 - 1
print(part_2_answer)
