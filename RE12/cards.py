import random
from functools import reduce
from cards import SUITS, RANKS, create_deck, deal_hands, choose, player_order

def choose_remove(items):
    c = choose(items)
    items.remove(c)
    return c

def card_value(card) -> int:
    suit, rank = card
    value = 11 if rank == "A" else 10 if rank.isalpha() else int(rank)
    return 2*value if suit == "♠" or suit == "♣" else value

def play(seed) -> None:
    random.seed(seed)

    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)
    points = {p: 0 for p in names}

    while hands[start_player]:
        round_points = {name: card_value(choose_remove(hands[name])) for name in turn_order}
        m = max(round_points.values())
        for n, p in round_points.items():
            if p == m:
                points[n] += 1

    m = max(points.values())
    return " ".join(n for n, p in points.items() if p == m)