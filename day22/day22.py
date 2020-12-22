import copy

from common.common import get_all_text


class Player:
    def __init__(self, data: str):
        lines = data.split('\n')
        self.id = lines[0][-2]
        self.cards = [int(x) for x in lines[1:]]


def get_winner(player1: Player, player2: Player):
    while len(player1.cards) > 0 and len(player2.cards) > 0:
        player1_card = player1.cards.pop(0)
        player2_card = player2.cards.pop(0)
        if player1_card > player2_card:
            player1.cards.extend([player1_card, player2_card])
        else:
            player2.cards.extend([player2_card, player1_card])
    return player1 if len(player1.cards) > 0 else player2


def get_winner2(player1: Player, player2: Player):
    player1_mem = set()
    player2_mem = set()
    while len(player1.cards) > 0 and len(player2.cards) > 0:
        if ','.join(map(str, player1.cards)) in player1_mem and ','.join(map(str, player2.cards)) in player2_mem:
            return player1
        player1_mem.add(','.join(map(str, player1.cards)))
        player2_mem.add(','.join(map(str, player2.cards)))
        player1_card = player1.cards.pop(0)
        player2_card = player2.cards.pop(0)

        if player1_card <= len(player1.cards) and player2_card <= len(player2.cards):
            player1_copy = copy.deepcopy(player1)
            player1_copy.cards = player1_copy.cards[:player1_card]
            player2_copy = copy.deepcopy(player2)
            player2_copy.cards = player2_copy.cards[:player2_card]
            if get_winner2(player1_copy, player2_copy).id == player1.id:
                player1.cards.extend([player1_card, player2_card])
            else:
                player2.cards.extend([player2_card, player1_card])
        else:
            if player1_card > player2_card:
                player1.cards.extend([player1_card, player2_card])
            else:
                player2.cards.extend([player2_card, player1_card])
    return player1 if len(player1.cards) > 0 else player2


if __name__ == '__main__':
    player1, player2 = [Player(x) for x in get_all_text('in.txt').split('\n\n')]
    # winner = get_winner(player1, player2)
    winner = get_winner2(player1, player2)
    print(sum(x * (i + 1) for i, x in enumerate(winner.cards[::-1])))
