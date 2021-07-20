def override(l1, l2):
    first_elements = list(map(lambda x: x[0], l2))
    return sorted(list(filter(lambda x: x[0] not in first_elements, l1)) + l2, key=lambda x: x[0])