def sort_leaders(records):
    records = sorted(records, key=lambda x: x[0])
    records = sorted(records, key=lambda x: len(x[1]))
    records = sorted(records, key=lambda x: max(x[1]), reverse=True)
    return tuple(records)
