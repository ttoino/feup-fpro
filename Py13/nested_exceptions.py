def nested_exceptions(tree):
    if callable(tree):
        try:
            tree()
        except:
            return True
        else:
            return False
    return tuple(map(nested_exceptions, tree))