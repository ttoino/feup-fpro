def validate(grade):
    return (type(grade) == int or type(grade) == float) and 0 <= grade <= 100
