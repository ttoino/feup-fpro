def fight(heroes, villain):
    for hero in heroes:
        if hero["category"] != villain["category"]:
            continue

        if villain["health"] > hero["health"]:
            villain["health"] -= hero["health"]//2
            continue

        return f"{ hero['name'] } defeated the villain and now has a score of {hero['score'] + 1}"

    return f"{villain['name']} prevailed with {villain['health']:.1f}HP left"
