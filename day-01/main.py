

with open("input.txt") as f:
    lines = f.readlines()
    inventories = []
    calories = 0
    for line in lines:
        item = line
        if item.replace("\n", "") != "":
            calories += int(item)
        else:
            inventories.append(calories)
            calories = 0

    inventories.sort(reverse=True)
    print(sum(inventories))
