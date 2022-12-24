

with open("input.txt") as f:
    lines = f.readlines()
    games = [game.replace("\n", "").split(" ") for game in lines]

move_info = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors'
}

goal_info = {
    'X': 'Lose',
    'Y': 'Draw',
    'Z': 'Win'
}

point_info = {
    'Game': {
        'Win': 6,
        'Draw': 3,
        'Loss': 0
    },
    'Move': {
        'Rock': 1,
        'Paper': 2,
        'Scissors': 3
    }
}

win_info = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}

lose_info = {
    'Rock': 'Paper',
    'Paper': 'Scissors',
    'Scissors': 'Rock'
}

my_points = 0

for game in games:
    [opponent, me] = game

    goal = goal_info[me]
    if goal == "Win":
        my_move = lose_info[move_info[opponent]]
    elif goal == "Draw":
        my_move = move_info[opponent]
    else:
        my_move = win_info[move_info[opponent]]

    win = win_info[my_move] == move_info[opponent]
    draw = my_move == move_info[opponent]

    # Points for move
    my_points += point_info['Move'][my_move]

    # Points for outcome
    if win:
        my_points += point_info['Game']['Win']
    elif draw:
        my_points += point_info['Game']['Draw']
    else:
        my_points += point_info['Game']['Loss']

print(my_points)
