def genealogy(l):
    d = dict()
    
    for (name, rel) in l:
        if rel in d:
            d[rel].append(name)
        else:
            d[rel] = [name]
    
    return sorted([(sorted(v), k) for (k, v) in d.items()], key=lambda x: ["sibling", "parent", "cousin", "grandparent"].index(x[1]))