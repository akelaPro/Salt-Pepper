def rps_game_winner(args):
    if len(args) != 2:
        raise ValueError('WrongNumberOfPlayersError')

    hands = ['R', 'P', 'S']
    player_1, hand_1 = args[0]
    player_2, hand_2 = args[1]

    if hand_1 not in hands or hand_2 not in hands:
        raise Exception('NoSuchStrategyError')
    if hand_1 == hand_2:
        return to_str(player_1, hand_1)
    
    winning_combinations = {
    'P': 'R',
    'R': 'S',
    'S': 'P'
        }

    if winning_combinations[hand_1] == hand_2:
        return to_str(player_1, hand_2)
    else:
        return to_str(player_2, hand_2)
    
def to_str(arg1, arg2):
    return f"'{arg1} {arg2}'"
