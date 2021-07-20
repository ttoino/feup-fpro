def sort_grades(records):
    records = sorted(records, key=lambda x: x[1])
    records = sorted(records, key=lambda x: x[0])
    return tuple(sorted(records, key=lambda x: sum(x[2])/len(x[2]), reverse=True))