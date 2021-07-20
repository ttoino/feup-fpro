def get_positions(sentence, word_list):
    s = sentence.split()

    try:
        return " ".join(map(lambda x: str(word_list.index(x)), s))
    except:
        return ""