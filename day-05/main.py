import re

with open("input.txt") as f:
    lines = f.readlines()
    actions = [re.findall("\d+", action.replace("\n", ""))
               for action in lines]

##############
### PART 1 ###
##############
container_map = {
    1: ['J','H','G','M','Z','N','T','F'],
    2: ['V','W','J'],
    3: ['G','V','L','J','B','T','H'],
    4: ['B','P','J','N','C','D','V','L'],
    5: ['F','W','S','M','P','R','G'],
    6: ['G','H','C','F','B','N','V','M'],
    7: ['D','H','G','M','R'],
    8: ['H','N','M','V','Z','D'],
    9: ['G','N','F','H'],
}

for action in actions:
    [move, from_, to] = [int(a) for a in action]

    for m in range(move):
        container = container_map[from_].pop()
        # print('container: ', container)
        container_map[to].append(container)

answer_p1 = ""
for stack in container_map:
    answer_p1 += container_map[stack][-1]
print(answer_p1)


##############
### PART 2 ###
##############
container_map = {
    1: ['J','H','G','M','Z','N','T','F'],
    2: ['V','W','J'],
    3: ['G','V','L','J','B','T','H'],
    4: ['B','P','J','N','C','D','V','L'],
    5: ['F','W','S','M','P','R','G'],
    6: ['G','H','C','F','B','N','V','M'],
    7: ['D','H','G','M','R'],
    8: ['H','N','M','V','Z','D'],
    9: ['G','N','F','H'],
}

for action in actions:
    [move, from_, to] = [int(a) for a in action]
    # Container(s) to move
    containers = container_map[from_][-move:]
    # Remove from original location
    container_map[from_] = container_map[from_][:len(
        container_map[from_])-move]
    # Add to new location
    container_map[to] = container_map[to] + containers

answer_p2 = ""
for stack in container_map:
    answer_p2 += container_map[stack][-1]
print(answer_p2)
