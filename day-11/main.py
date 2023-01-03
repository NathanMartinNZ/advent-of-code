import math

with open("input.txt") as f:
    lines = [line.replace("\n", "").strip() for line in f.readlines() + ["\n"]]
    idxs = [i for i, line in enumerate(lines) if line == ""]
    turns_raw = [[line for line in lines[i:j] if line != ""] for i, j in zip([0]+idxs, idxs)]


### Part 1 ###
def set_attribs(turn, idx):
    items = turn[1].replace("Starting items: ", "").split(", ")
    items = [int(item) for item in items]

    operation_num = -1
    if "old * old" in turn[2]:
        operation_type = "multiply"
    elif "old + old" in turn[2]:
        operation_type = "add"
    elif "*" in turn[2]:
        operation_type = "multiply"
        operation_num = int(turn[2].replace("Operation: new = old * ", ""))
    else:
        operation_type = "add"
        operation_num = int(turn[2].replace("Operation: new = old + ", ""))

    test = int(turn[3].replace("Test: divisible by ", ""))
    test_pass = int(turn[4].replace("If true: throw to monkey ", ""))
    test_fail = int(turn[5].replace("If false: throw to monkey ", ""))

    return {
        "id": idx,
        "items": items,
        "operation_num": operation_num,
        "operation_type": operation_type,
        "test": test,
        "test_pass": test_pass,
        "test_fail": test_fail,
        "inspection_count": 0
    }

def run(rounds, reduce_worry):
    turns = []
    for idx, turn in enumerate(turns_raw):
        turns.append(set_attribs(turn, idx))

    test_modulo = math.prod([turn["test"] for turn in turns])

    for _ in range(rounds):
        for idx, turn in enumerate(turns):
            items_copy = turn["items"].copy()
            for item in items_copy:
                item %= test_modulo
                turn["inspection_count"] += 1
                num = turn["operation_num"] if turn["operation_num"] != -1 else item
                item = item * num if turn["operation_type"] == "multiply" else item + num
                if reduce_worry: item = math.floor(item/3)

                if item % turn["test"] == 0:
                    turns[turn["test_pass"]]["items"].append(item)
                else:
                    turns[turn["test_fail"]]["items"].append(item)
                turn["items"].pop(0)
    
    sorted_total_counts = sorted(turns, key=lambda m: m["inspection_count"], reverse=True)
    return  sorted_total_counts[0]["inspection_count"] * sorted_total_counts[1]["inspection_count"]


part_1_answer = run(20, True) # rounds, reduce_worry
print(part_1_answer)

part_2_answer = run(10000, False)
print(part_2_answer)